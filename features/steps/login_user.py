from behave import given, step, then, when


@given('Exists a user "admin" with password "admin"')
def create_user(context):
    user = context.db.create_user(username="admin", password="admin")
    user.save()


@given('I login as user "admin" with password "admin"')
def login_user_admin_admin(context):
    login(context, "admin", "admin")


def login(context, username, password):
    context.browser.visit(context.get_url("/accounts/login"))
    context.browser.fill("username", username)
    context.browser.fill("password", password)


@when("I click on the login button")
def click_login_button(context):
    form = context.browser.find_by_tag("form").first
    form.find_by_value("login").click()


@then("I should see the main page")
def check_we_are_on_main_page(context):
    assert context.browser.url == context.get_url("/")


@given('I login as user "admin" with password "notadmin"')
def login_as_admin_notadmin(context):
    login(context, "admin", "notadmin")


@then("I should see the login page")
def see_login_page(context):
    assert context.browser.url == context.get_url("/login/")


@step("I should see an error message")
def see_error_message(context):
    assert context.browser.is_element_present_by_id("error_message")


@step("I should see the logout button on the top right corner of the navbar")
def step_impl(context):
    context.browser.visit(context.get_url("/"))
    assert context.browser.is_element_present_by_id("logout")
