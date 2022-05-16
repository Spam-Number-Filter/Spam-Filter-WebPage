from behave import step, then, when


@when("I click on the comment")
def click_comment(context):
    context.browser.find_by_id("message").click()


@step("I write a comment")
def write_comment(context):
    message_input = context.browser.find_by_id("message")
    new_title = context.table.rows[0]["comment"]
    message_input.fill(new_title)


@step('I press "Submit"')
def click_submit(context):
    context.browser.find_by_id("submitbutton").click()


@then("I should see the comment")
def see_comment(context):
    comment = context.table.rows[0]["comment"]
    assert context.browser.is_text_present(comment)


@step("I should still be on the post page")
def still_on_post(context):
    no_post_browser_url = context.browser.url[:-2]
    assert no_post_browser_url == context.get_url("/post/")
