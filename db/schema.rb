# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# Note that this schema.rb definition is the authoritative source for your
# database schema. If you need to create the application database on another
# system, you should be using db:schema:load, not running all the migrations
# from scratch. The latter is a flawed and unsustainable approach (the more migrations
# you'll amass, the slower it'll run and the greater likelihood for issues).
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 20181030005605) do

  create_table "backgrounds", force: :cascade do |t|
    t.string "name"
    t.float "price"
    t.string "image"
    t.integer "game_id"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["game_id"], name: "index_backgrounds_on_game_id"
  end

  create_table "cards", force: :cascade do |t|
    t.string "name"
    t.float "price"
    t.string "image"
    t.boolean "foil"
    t.integer "game_id"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["game_id"], name: "index_cards_on_game_id"
  end

  create_table "comments", force: :cascade do |t|
    t.text "description"
    t.integer "gamer_id"
    t.integer "game_id"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "companies", force: :cascade do |t|
    t.string "name"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "companies_games", id: false, force: :cascade do |t|
    t.integer "company_id", null: false
    t.integer "game_id", null: false
  end

  create_table "emotes", force: :cascade do |t|
    t.string "name"
    t.float "price"
    t.string "image"
    t.integer "game_id"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["game_id"], name: "index_emotes_on_game_id"
  end

  create_table "gamers", force: :cascade do |t|
    t.string "gamername"
    t.string "email"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.string "password_digest"
    t.string "user_type"
    t.boolean "admin", default: false
  end

  create_table "gamers_games", id: false, force: :cascade do |t|
    t.integer "game_id", null: false
    t.integer "gamer_id", null: false
  end

  create_table "games", force: :cascade do |t|
    t.integer "steam_id"
    t.string "name"
    t.float "price"
    t.date "release_date"
    t.string "description"
    t.string "image"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "games_genres", id: false, force: :cascade do |t|
    t.integer "game_id", null: false
    t.integer "genre_id", null: false
  end

  create_table "genres", force: :cascade do |t|
    t.string "name"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "graphics", force: :cascade do |t|
    t.string "name"
    t.integer "rank"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "likes", force: :cascade do |t|
    t.boolean "like"
    t.integer "gamer_id"
    t.integer "game_id"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "memories", force: :cascade do |t|
    t.string "name"
    t.integer "rank"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "messages", force: :cascade do |t|
    t.text "content"
    t.integer "gamer_id"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "processors", force: :cascade do |t|
    t.string "name"
    t.integer "rank"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "requests", force: :cascade do |t|
    t.integer "steam_id"
    t.string "status"
    t.integer "gamer_id"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["gamer_id"], name: "index_requests_on_gamer_id"
  end

  create_table "system_requirements", force: :cascade do |t|
    t.integer "game_id"
    t.integer "processor_id"
    t.integer "graphic_id"
    t.integer "memory_id"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["game_id"], name: "index_system_requirements_on_game_id"
    t.index ["graphic_id"], name: "index_system_requirements_on_graphic_id"
    t.index ["memory_id"], name: "index_system_requirements_on_memory_id"
    t.index ["processor_id"], name: "index_system_requirements_on_processor_id"
  end

end
