class AddKeyword2AndRelevance2ToPromotions < ActiveRecord::Migration
  def change
    add_column :promotions, :keyword2, :string
    add_column :promotions, :relevance2, :float
  end
end
