from behave import given, step, then, when


@given('Exists a user "admin" with password "admin"')
def create_user(context):
    user = context.db.create_user(username="admin", password="admin")
    user.save()


@given('I login as user "admin" with password "admin"')
def login_user_admin_admin(context):
    context.browser.visit(context.get_url("/accounts/login"))
    context.browser.fill("username", "admin")
    context.browser.fill("password", "admin")


@when("I click on the login button")
def click_login_button(context):
    form = context.browser.find_by_tag("form").first
    form.find_by_value("login").click()


@then("I should see the main page")
def check_we_are_on_main_page(context):
    assert context.browser.url == context.get_url("/")


@given('I login as user "admin" with password "notadmin"')
def login_as_admin_notadmin(context):
    raise NotImplementedError(
        'STEP: Given I login as user "admin" with password "notadmin"'
    )


@then("I should see the login page")
def see_login_page(context):
    raise NotImplementedError("STEP: Then I should see the login page")


@step("I should see an error message")
def see_error_message(context):
    raise NotImplementedError("STEP: And I should see an error message")


@step("I should see the logout button on the top right corner of the navbar")
def step_impl(context):
    context.browser.visit(context.get_url("/"))
    assert context.browser.is_element_present_by_id("logout")
