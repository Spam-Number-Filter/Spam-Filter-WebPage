from behave import then, when


@when("I click on like button")
def click_like(context):
    context.browser.find_by_id("like_button").first.click()


@then("I should be redirected to the same post page")
def assert_redirect_post_page(context):
    assert context.browser.find_by_id("like_button")


@then("I should see one more like on the post")
def check_like(context):
    assert context.browser.find_by_id("likes_h5").text == "1"


@then("I should see the post has not likes")
def check_no_like(context):
    assert context.browser.find_by_id("likes_h5").text == "0"
