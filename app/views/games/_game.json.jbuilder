json.extract! game, :id, :steam_id, :name, :price, :release_date, :description, :image, :created_at, :updated_at
json.url game_url(game, format: :json)
