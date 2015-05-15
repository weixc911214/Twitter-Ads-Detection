json.array!(@promotions) do |promotion|
  json.extract! promotion, :id, :username, :password, :keyword
  json.url promotion_url(promotion, format: :json)
end
