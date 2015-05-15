class CreateTwitters < ActiveRecord::Migration
  def change
    create_table :twitters do |t|
      t.string :username
      t.string :content
      t.string :keyword

      t.timestamps null: false
    end
  end
end
