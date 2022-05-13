from behave import step, then, when


@when("I click on the delete button")
def click_delete(context):
    context.browser.find_by_css(".btn-danger").first.click()


@then("I sould be redirected to the home page")
def assert_redirect_home_page(context):
    assert context.browser.url == context.get_url("/")


@step("I go to trendy")
def go_trendy(context):
    context.browser.visit(context.get_url("/trendy"))


@then("I shouldn't see my post")
def step_impl(context):
    assert context.browser.is_text_not_present("Post title")
