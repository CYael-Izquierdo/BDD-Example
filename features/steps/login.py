from behave import given, when, then
from pageObject import pageObject as Po
from features.steps.constants import Constants


@given('a web browser is at the redmine login page')
def step_impl(context):
    context.browser.get(Constants.BASE_URL)
    base_logout_po = Po.BaseLogoutPO(context.browser)
    base_logout_po.goto_login()


@when('I fill username with {username}, password with {password} and press login')
def step_impl(context, username, password):
    login_po = Po.LoginPO(context.browser)
    login_po.login(username, password)


@then('I should see logged in as {username}')
def step_impl(context, username):
    base_login_po = Po.BaseLoginPO(context.browser)
    assert (username == base_login_po.get_username())


@then('I should see "Invalid user or password" alert')
def step_impl(context):
    login_po = Po.LoginPO(context.browser)
    assert ('Invalid user or password' == login_po.get_flash_error_text())
