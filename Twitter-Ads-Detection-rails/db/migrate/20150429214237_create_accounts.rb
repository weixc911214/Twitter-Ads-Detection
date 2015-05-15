class CreateAccounts < ActiveRecord::Migration
  def change
    create_table :accounts do |t|
      t.string :username
      t.string :password
      t.string :keyword
      t.string :token
      t.string :secret

      t.timestamps null: false
    end
  end
end
