from behave import fixture, use_fixture
from fixtures import fixture
from testlink.tlbehave import TLBehave


def before_all(context):
    context._root['new_build_id'] = None
    context.asd = 5


def before_scenario(context, scenario):
    if 'fixture.browser.chrome' in scenario.tags:
        use_fixture(fixture.browser_chrome, context)
    if 'fixture.browser.safari' in scenario.tags:
        use_fixture(fixture.browser_safari, context)
    if 'fixture.browser.firefox' in scenario.tags:
        use_fixture(fixture.browser_firefox, context)


def after_scenario(context, scenario):
    # tl.project.testplanid
    for tag in scenario.tags:
        if 'tl' in tag:
            TLBehave.report_test_case_result(context, scenario, tag)


def after_step(context, step):
    if step.status.name == 'failed':
        context.browser.save_screenshot(
            'screenshot/{}-{}.png'.format(step.keyword, step.name).replace(' ', '-').lower())



