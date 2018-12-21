from behave import fixture, use_fixture
from fixtures import fixture


def before_scenario(context, scenario):
    if 'fixture.browser.chrome' in scenario.tags:
        use_fixture(fixture.browser_chrome, context)
