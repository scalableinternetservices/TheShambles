import csv
import json
import lorem
import random
import urllib


IDfile = 'IDs.csv' # file containing steam ids and names

numGames = 0 # loop control

gameCount = 100 # number of games
gamerCount = 10 # number of gamers
processorCount = 10 # number of processors
graphicCount = 10 # number of graphics card
memoryCount = 10 # number of memories

Games = [] # Game model data

genres = [ # dummy collection of genres
            'adventure', 'action', 'rpg', 'simulation', 'indie', 'strategy', 'fps', 'sports',
            'mmo', 'racing', 'puzzle', 'survival', 'arcade', 'retro', 'classic', 'third person',
            'tactical', 'war', 'physics', 'rts', 'stealth', 'defense', 'board', 'detective',
        ]

companies = [ # dummy collection of companies
            'nintendo', 'valve', 'rockstar', 'ea', 'activision', 'sony', 'ubisoft', 'sega', 'bioware',
            'square enix', 'capcom', 'microsoft', 'bandai', 'konami', 'insomniac', 'infinity ward',
            'take-two', 'gameloft', 'blizzard', 'zynga', 'bethesda', 'lucasarts', 'atari', 'popcap',
            'relic',
        ]

# takes appid (aka steamid) of a game as parameter and returns its information
def getGameDetails(appid):
    url = 'http://store.steampowered.com/api/appdetails?appids={0}&cc=us&l=en'.format(appid)
    response = urllib.urlopen(url)
    data = json.loads(response.read())

    # if API has no data leave
    if data[appid]['success'] == False:
        return None

    print('data from {0}'.format(url))

    game = {}

    game['steam_id'] = appid
    game['name'] = data[appid]['data']['name']
    
    # if price not available leave
    if 'price_overview' in data[appid]['data']:
        game['price'] = data[appid]['data']['price_overview']['final'] / 100.0
    else:
        return None

    game['release_date'] = data[appid]['data']['release_date']['date']

    # dummy description
    # game['description'] = data[appid]['data']['detailed_description']
    game['description'] = lorem.paragraph() 

    # dummy genres
    genre_count = random.randint(1, 8)
    genre_ids = range(len(genres))
    random.shuffle(genre_ids)
    game['genre_ids'] = genre_ids[0:genre_count]

    # dummy companies
    company_count = random.randint(1, 5)
    company_ids = range(len(companies))
    random.shuffle(company_ids)
    game['company_ids'] = company_ids[0:company_count]

    # dummy gamers
    gamer_count = random.randint(1, gamerCount + 1)
    gamer_ids = range(gamerCount)
    random.shuffle(gamer_ids)
    game['gamer_ids'] = gamer_ids[0:gamer_count]

    game['image'] = data[appid]['data']['header_image']
    return game

# generates seed file from: Games
def generateSeedFile(filename='seeds.rb'):
    with open(filename, 'w') as fh:
        fh.write('# for clean setup please run the following commands:\n')
        fh.write('#   rails db:drop\n')
        fh.write('#   rails db:migrate\n')
        fh.write('#   rails db:seed\n\n')
        fh.write('Game.destroy_all\n')
        fh.write('Genre.destroy_all\n\n')

        #gamers
        fh.write('gamers = Gamer.create([\n')
        fh.write("\t{gamername: 'admin', email: 'admin@admin.com', password_digest: '$2a$10$unFFch9BQLTGgRN.lrJU6OfUScH6WeRPBXYm/3RXjwLDXVCwZ3q8S'},\n")
        for x in range(1, gamerCount + 1):
            fh.write("\t{{gamername: 'gamer{0}', email: 'gamer{0}@gamer.com', password_digest: '{1}'}},\n".format(x, "$2a$10$unFFch9BQLTGgRN.lrJU6OfUScH6WeRPBXYm/3RXjwLDXVCwZ3q8S"))
        fh.write('])\n\n')

        # genres
        fh.write('genres = Genre.create([\n')
        for genre in genres:
            fh.write("\t{{name: '{0}'}},\n".format(genre))
        fh.write('])\n\n')

        # companies
        fh.write('companies = Company.create([\n')
        for company in companies:
            fh.write("\t{{name: '{0}'}},\n".format(company))
        fh.write('])\n\n')

        #games
        fh.write('games = Game.create([\n')
        for game in Games:
            #genre
            genre_ids = '['
            for genre_id in game['genre_ids']:
                genre_ids += 'genres[{0}].id, '.format(genre_id)
            genre_ids += ']'
            #company
            company_ids = '['
            for company_id in game['company_ids']:
                company_ids += 'companies[{0}].id, '.format(company_id)
            company_ids += ']'
            #gamer
            gamer_ids = '['
            for gamer_id in game['gamer_ids']:
                gamer_ids += 'gamers[{0}].id, '.format(gamer_id)
            gamer_ids += ']'
            fh.write("\t{{steam_id: {0}, name: '{1}', price: {2}, release_date: '{3}', description: '{4}', image: '{5}', genre_ids: {6}, company_ids: {7}, gamer_ids: {8}}},\n".format(game['steam_id'], game['name'].replace("'", "\\'").encode('utf-8'), game['price'], game['release_date'], game['description'].encode('utf-8'), game['image'], genre_ids, company_ids, gamer_ids))
        fh.write('])\n\n')

#        #game ratings
#        for x in range(len(Games)):
#            fh.write("games[{0}].game_ratings ".format(x))
#            user_ids = range(1, gamerCount + 1)
#            random.shuffle(user_ids)
#            for y in user_ids[0:random.randint(1, gamerCount)]:
#                fh.write("<< GameRating.new(gamer: gamers[{0}], rating: {1}) ".format(y, random.randint(1, 6)))
#            fh.write('\n')
#        fh.write('\n\n')

        #game comments
        for x in range(len(Games)):
            fh.write("games[{0}].comments ".format(x))
            user_ids = range(1, gamerCount + 1)
            random.shuffle(user_ids)
            for y in user_ids[0:random.randint(1, gamerCount)]:
                fh.write("<< Comment.new(gamer: gamers[{0}], description: '{1}') ".format(y, lorem.paragraph()))
            fh.write('\n')
        fh.write('\n\n')

        #game requests
        requested_ids = [958000, 958010, 958030, 958060, 958240, 958300, 958310, 958420, 958430, 958790]
        fh.write("requests = Request.create([\n")
        for x in range(1, len(requested_ids) + 1):
            # x holds user id (x + 1 to skip over admin), x - 1 holds index to requested id
            fh.write("\t{{steam_id: {0}, status: '{1}', gamer_id: {2}}},\n".format(requested_ids[x - 1], "pending", (x + 1)))
        fh.write("])")
        fh.write("\n\n")

        #backgrounds
        fh.write("backgrounds = Background.create([\n")
        fh.write("\t{name: 'All Tidied Up', price: 0.03, image: 'https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxH5rd9eDAjcFyv45SRYAFMIcKL_PArgVSL403ulRUWEndVKv1gZmLBQ07IwAA777zewE40vLJJjsbvd_nx4LdwvKnN-jQwmlQuJVz0urE9oij2Rq-uxQsQbMDMg', game_id: 1},\n")
        fh.write("])")
        fh.write("\n\n")

        #emotes
        fh.write("emotes = Emote.create([\n")
        fh.write("\t{name: 'shield_orochi4', price: 0.94, image: 'https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxH5rd9eDAjcFyv45SRYAFMIcKL_PArgVSL403ulRUWEndVKv1hJ6GBQ07fFRR5uP9fl5ji6GQJm4VtYvgw9bZk6akZLjUw24HusRz2rjErYql2BqkpRQNCzaaig/360fx360f', game_id: 1},\n")
        fh.write("])")
        fh.write("\n\n")

        #cards
        fh.write("cards = Card.create([\n")
        fh.write("\t{name: 'Salien Spaceship', price: 0.05, image: 'https://steamcommunity-a.akamaihd.net/economy/image/IzMF03bk9WpSBq-S-ekoE33L-iLqGFHVaU25ZzQNQcXdA3g5gMEPvUZZEaiHLrVJRsl8vGuCUY7Cjc9ehDNVzDMOfXSviSQrcex4NM6b8wT3qOeDV0fnaTTBPCnQDBhhEOIJYGXQ_GHx5b7HFD7IErslRgwFfKJR9WVOP87cOhU_0tEM8jO9wxYpGEN9PM9Wd0m5xWYXNK8awSwTIs5fnXalcpLfjVZnPRU_Wuq2A-nKa4DxwXkgVU41TKEfYI6VsSG5rpPzaOnGc68hIvw2RD05Cio/120x140', foil: false, game_id: 1},\n")
        fh.write("])")
        fh.write("\n\n")

        #processor
        fh.write("processors = Processor.create([\n")
        for x in range(1, processorCount + 1):
            fh.write("\t{{name: 'Processor {0}', rank: {0}}},\n".format(x))
        fh.write("])")
        fh.write("\n\n")

        #graphic
        fh.write("graphics = Graphic.create([\n")
        for x in range(1, graphicCount + 1):
            fh.write("\t{{name: 'Graphic {0}', rank: {0}}},\n".format(x))
        fh.write("])")
        fh.write("\n\n")

        #memory
        fh.write("memories = Memory.create([\n")
        for x in range(1, memoryCount + 1):
            fh.write("\t{{name: 'Memory {0}', rank: {0}}},\n".format(x))
        fh.write("])")
        fh.write("\n\n")

        #system rquirements
        fh.write("system_requirements = SystemRequirement.create([\n")
        for x in range(1, gameCount + 1):
            fh.write("\t{{game_id: {0}, processor_id: {1}, graphic_id: {2}, memory_id: {3}}},\n".format(x, random.randint(1, processorCount + 1), random.randint(1, graphicCount + 1), random.randint(1, memoryCount + 1)))
        fh.write("])")
        fh.write("\n\n")


if __name__ == '__main__':
    with open(IDfile) as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            game = getGameDetails(row['appid'])
            if game == None:
                pass
            else:
                Games.append(game)
                numGames += 1
                if numGames == gameCount:
                    break
    generateSeedFile('seeds.rb')

