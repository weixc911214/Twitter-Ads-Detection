class AddKeyword3AndRelevance3ToPromotions < ActiveRecord::Migration
  def change
    add_column :promotions, :keyword3, :string
    add_column :promotions, :relevance3, :float
  end
end
