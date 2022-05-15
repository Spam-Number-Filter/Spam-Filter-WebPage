from behave import given, step, then, use_step_matcher, when

use_step_matcher("re")


@given("I am on the post page")
def post_page(context):
    # It's for better understanding,
    # user is already on the post page
    pass


@when("I click on the modify button")
def click_modify(context):
    context.browser.find_by_id("modify").first.click()


@step('I fill in "title" with "New title"')
def fill_title(context):
    new_title = context.table.rows[0]["title"]
    title_input = context.browser.find_by_name("title")
    title_input.fill(new_title)


@step('I click on the "Submit" button')
def click_submit(context):
    context.browser.find_by_id("Submit").first.click()


@then("I should see the post edit page")
def see_edit_page(context):
    # Ignore the post number. Ex: /post/edit/[1/]
    no_post_browser_url = context.browser.url[:-2]
    assert no_post_browser_url == context.get_url("/post/edit/")


@step("There should be no input in any field")
def no_edit_input(context):
    title_input = context.browser.find_by_name("title")
    assert title_input.value == ""
    message_input = context.browser.find_by_name("message")
    assert message_input.value == ""


@then("I should the post with the new title and message")
def new_title_message(context):
    # Ignore the post number. Ex: /posts/[1/]
    no_post_browser_url = context.browser.url[:-2]
    assert no_post_browser_url == context.get_url("/posts/")
    assert context.browser.is_text_present("New title")
    assert context.browser.is_text_present("New message")


@step('I fill in "message" with "New message"')
def fill_message(context):
    new_message = context.table.rows[0]["message"]
    message_input = context.browser.find_by_name("message")
    message_input.fill(new_message)
