from behave import fixture, use_fixture
from fixtures import fixture
from behave.model_core import Status


def before_scenario(context, scenario):
    if 'fixture.browser.chrome' in scenario.tags:
        use_fixture(fixture.browser_chrome, context)
    if 'fixture.browser.safari' in scenario.tags:
        use_fixture(fixture.browser_safari, context)
    if 'fixture.browser.firefox' in scenario.tags:
        use_fixture(fixture.browser_firefox, context)


def after_step(context, step):
    if step.status.name == 'failed':
        context.browser.save_screenshot('screenshot/{} {}.png'.format(step.keyword, step.name).replace(' ', '-').lower())
