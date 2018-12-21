from behave import given, when, then
from pageObject import pageObject as Po

base_url = 'http://192.168.64.2/'


@given('I am on home page')
def step_impl(context):
    context.browser.get(base_url)
