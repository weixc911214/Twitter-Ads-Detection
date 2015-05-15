json.array!(@twitters) do |twitter|
  json.extract! twitter, :id, :username, :content, :keyword
  json.url twitter_url(twitter, format: :json)
end
