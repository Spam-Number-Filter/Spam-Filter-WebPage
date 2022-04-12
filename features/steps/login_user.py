from behave import given, when, then

@given(u'Exists a user "user" with password "password"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Exists a user "user" with password "password"')


@given(u'I login as user "user" with password "password"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I login as user "user" with password "password"')


@when(u'I register restaurant')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I register restaurant')


@then(u'I\'m viewing the details page for restaurant by "user"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I\'m viewing the details page for restaurant by "user"')


@then(u'There are 1 restaurants')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then There are 1 restaurants')