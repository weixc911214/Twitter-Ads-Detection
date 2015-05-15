# encoding: UTF-8
# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# Note that this schema.rb definition is the authoritative source for your
# database schema. If you need to create the application database on another
# system, you should be using db:schema:load, not running all the migrations
# from scratch. The latter is a flawed and unsustainable approach (the more migrations
# you'll amass, the slower it'll run and the greater likelihood for issues).
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 20150503205334) do

  create_table "accounts", force: :cascade do |t|
    t.string   "username",   limit: 255
    t.string   "password",   limit: 255
    t.string   "keyword",    limit: 255
    t.datetime "created_at",             null: false
    t.datetime "updated_at",             null: false
  end

  create_table "promotions", force: :cascade do |t|
    t.string   "username",        limit: 255
    t.datetime "created_at",                    null: false
    t.datetime "updated_at",                    null: false
    t.string   "content",         limit: 255
    t.string   "promoted_source", limit: 255
    t.text     "img_url",         limit: 65535
    t.string   "keyword1",        limit: 255
    t.float    "relevance1",      limit: 24
    t.string   "keyword2",        limit: 255
    t.float    "relevance2",      limit: 24
    t.string   "keyword3",        limit: 255
    t.float    "relevance3",      limit: 24
  end

  create_table "twitters", force: :cascade do |t|
    t.string "username", limit: 255
    t.text   "content",  limit: 65535
    t.string "keyword",  limit: 255
  end

end
