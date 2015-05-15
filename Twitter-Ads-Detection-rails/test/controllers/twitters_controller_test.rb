require 'test_helper'

class TwittersControllerTest < ActionController::TestCase
  setup do
    @twitter = twitters(:one)
  end

  test "should get index" do
    get :index
    assert_response :success
    assert_not_nil assigns(:twitters)
  end

  test "should get new" do
    get :new
    assert_response :success
  end

  test "should create twitter" do
    assert_difference('Twitter.count') do
      post :create, twitter: { content: @twitter.content, keyword: @twitter.keyword, username: @twitter.username }
    end

    assert_redirected_to twitter_path(assigns(:twitter))
  end

  test "should show twitter" do
    get :show, id: @twitter
    assert_response :success
  end

  test "should get edit" do
    get :edit, id: @twitter
    assert_response :success
  end

  test "should update twitter" do
    patch :update, id: @twitter, twitter: { content: @twitter.content, keyword: @twitter.keyword, username: @twitter.username }
    assert_redirected_to twitter_path(assigns(:twitter))
  end

  test "should destroy twitter" do
    assert_difference('Twitter.count', -1) do
      delete :destroy, id: @twitter
    end

    assert_redirected_to twitters_path
  end
end
