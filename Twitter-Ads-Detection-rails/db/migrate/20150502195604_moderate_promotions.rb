class ModeratePromotions < ActiveRecord::Migration
  def change
    add_column :promotions, :content, :string
    remove_column :promotions, :password, :string
  end
end
