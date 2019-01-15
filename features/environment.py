from behave import fixture, use_fixture
from fixtures import fixture
from testlink.testlink import TestlinkAPIClient
from behave.model_core import Status
import base64


def before_scenario(context, scenario):
    if 'fixture.browser.chrome' in scenario.tags:
        use_fixture(fixture.browser_chrome, context)
    if 'fixture.browser.safari' in scenario.tags:
        use_fixture(fixture.browser_safari, context)
    if 'fixture.browser.firefox' in scenario.tags:
        use_fixture(fixture.browser_firefox, context)


def after_step(context, step):
    if step.status.name == 'failed':
        context.browser.save_screenshot(
            'screenshot/{}-{}.png'.format(step.keyword, step.name).replace(' ', '-').lower())


def after_scenario(context, scenario):
    for tag in scenario.tags:
        if 'testplan' in tag:
            test_plan = tag.split('-')[1]

            if scenario.status.name != 'skipped':
                client = TestlinkAPIClient()
                tc_name = scenario.name.split('--')[0]
                tc_id = client.getTestCaseIDByName(tc_name)[0]['id']
                if scenario.status.name == 'passed':
                    scenario_status = 'p'
                else:
                    scenario_status = 'f'

                image_url = ''
                steps = []
                for idx, step in enumerate(scenario.steps):
                    notes = step.duration

                    if step.status.name == 'passed':
                        status = 'p'
                    elif step.status.name == 'failed':
                        status = 'f'
                        notes = '{} - {}'.format(notes, step.error_message)
                        image_url = 'screenshot/{}-{}.png'.format(step.keyword, step.name).replace(' ', '-').lower()
                    else:
                        status = 'f'

                    steps.append({
                        'step_number': idx + 1,
                        'result': status,
                        'notes': notes
                    })

                execution = client.reportTCResult(tc_id, 5, scenario_status, 'build 1', 'MacOS', scenario.duration, steps)
                # print(execution)

                if scenario.status.name == 'failed':
                    file = base64.b64encode(open(image_url, 'rb').read())
                    upload_attachmeent = client.uploadExecutionAttachment(execution[0]['id'], 'img.png', 'image/png', file,
                                                                      'Fail', 'Fail')
                    # print(upload_attachmeent)
