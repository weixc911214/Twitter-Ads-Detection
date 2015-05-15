class Promotion < ActiveRecord::Base
    belongs_to :account, foreign_key: 'username'
end
