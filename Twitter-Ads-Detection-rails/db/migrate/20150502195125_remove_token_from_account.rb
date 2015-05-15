class RemoveTokenFromAccount < ActiveRecord::Migration
  def change
    remove_column :accounts, :token, :string
    remove_column :accounts, :secret, :string
  end
end
