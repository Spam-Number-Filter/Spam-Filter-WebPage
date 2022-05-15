from behave import given, step, then, when


@given("I write a new comment")
def write_comment(context):
    context.browser.fill("message", "My own comment")
    context.browser.find_by_id("submit-button").click()


@when("I click on the delete comment button")
def click_delete(context):
    context.browser.find_by_css(".btn-outline-danger").first.click()


@then("I souldn't see my comment anymore")
def check_if_comment_is_present(context):
    assert context.browser.is_text_not_present("My own comment")


@given("I logout")
def logout(context):
    context.browser.find_by_id("logout").click()


@when('I login as user "admin" with password "admin"')
def login_user_admin_admin(context):
    login(context, "admin", "admin")


def login(context, username, password):
    context.browser.visit(context.get_url("/accounts/login/"))
    context.browser.fill("username", username)
    context.browser.fill("password", password)


@step("I add a comment to the first post")
def add_comment_as_admin(context):
    message = context.browser.find_by_name("message").first
    message.fill("Admin's comment")
    context.browser.find_by_id("submit-button").click()


@step("I go to the post")
def go_to_post(context):
    context.browser.visit(context.get_url("/trendy"))
    context.browser.find_by_css(".col-md-8").first.click()


@then("I shouldn't see a delete button inside admin's comment")
def assert_delete_btn_not_present_in_admin_comment(context):
    assert context.browser.is_element_not_present_by_css(".btn-outline-danger")
