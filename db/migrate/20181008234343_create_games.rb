class CreateGames < ActiveRecord::Migration[5.1]
  def change
    create_table :games do |t|
      t.integer :steam_id
      t.string :name
      t.float :price
      t.date :release_date
      t.string :description
      t.string :image

      t.timestamps
    end
  end
end
