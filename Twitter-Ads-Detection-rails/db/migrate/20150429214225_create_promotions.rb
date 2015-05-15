class CreatePromotions < ActiveRecord::Migration
  def change
    create_table :promotions do |t|
      t.string :username
      t.string :password
      t.string :keyword

      t.timestamps null: false
    end
  end
end
