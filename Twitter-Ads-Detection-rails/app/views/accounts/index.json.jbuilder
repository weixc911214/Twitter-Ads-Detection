json.array!(@accounts) do |account|
  json.extract! account, :id, :username, :password, :keyword, :token, :secret
  json.url account_url(account, format: :json)
end
