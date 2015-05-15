class AddKeyword1AndRelevance1ToPromotions < ActiveRecord::Migration
  def change
    add_column :promotions, :keyword1, :string
    add_column :promotions, :relevance1, :float
  end
end
