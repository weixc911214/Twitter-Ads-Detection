class Account < ActiveRecord::Base
    has_many :promotion, :dependent => :destroy
    has_many :twitter, :dependent => :destroy
    self.primary_key = 'username'
end
