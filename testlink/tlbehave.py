from testlink.testlink import TestlinkAPIClient
from datetime import datetime
import string
import base64
import random
import subprocess


class TLBehave:

    @staticmethod
    def report_test_case_result(context, scenario, tag):
        client = TestlinkAPIClient()

        # verifica si existe el proyecto, si no existe, lo crea
        test_project_name = tag.split('.')[1]
        try:
            test_project_id = client.getTestProjectByName(test_project_name)['id']
        except TypeError:
            test_project_id = TLBehave.create_new_test_project(client, test_project_name)[0]['id']

        # verifica si existe el test plan, si no existe, lo crea
        test_plan_name = tag.split('.')[2]
        try:
            test_plan_id = client.getTestPlanByName(test_project_name, test_plan_name)[0]['id']
        except KeyError:
            test_plan_id = \
                client.createTestPlan(test_plan_name, test_project_name, notes='test plan created by software')[0]['id']
        # si no se creo ninguna build para esta ejecución, se crea.
        if not context._root['new_build_id']:
            build_nro = len(client.getBuildsForTestPlan(test_plan_id))
            date = datetime.today().strftime('%d.%m.%y')
            build_name = "build-{}-{}".format(build_nro, date)
            response = client.createBuild(test_plan_id, build_name)
            context._root['new_build_id'] = response[0]['id']

        if scenario.status.name != 'skipped':
            tc_name = scenario.name.split('--')[0]
            tc_response = client.getTestCaseIDByName(tc_name)[0]

            if len(tc_response) == 2 and tc_response['code'] == 5030:
                # create test case and add to test plan
                # test_suit_id = client.getTestSuitesForTestPlan(test_plan)[0]['id']
                test_suits = client.getTestSuitesForTestPlan(test_plan_id)
                test_suit = ''

                for idx, ts in enumerate(test_suits):
                    if ts['name'] == scenario.feature.name:
                        test_suit = ts

                if not test_suit:
                    # test_suit = create_new_test_suit(scenario.feature, client, test_project_id)[0]
                    test_suit = client.createTestSuite(test_project_id, scenario.feature.name, 'created by software')[0]
                test_suit_id = test_suit['id']
                tc_steps = TLBehave._create_scenario_steps_to_tl(scenario.steps)
                new_tc = client.createTestCase(tc_name, test_suit_id, test_project_id, 'user',
                                               scenario.description, tc_steps)
                # print(new_tc)
                try:
                    platform_id = client.getTestPlanPlatforms(test_plan_id)[0]['id']
                except KeyError:
                    platform_id = ''
                aux = client.addTestCaseToTestPlan(test_plan_id, new_tc[0]['id'],
                                                   test_project_id, platformid=platform_id)
            else:
                # update test case
                tc_info = client.getTestCase(tc_response['id'])[0]
                tc_new_steps = None
                # ver si se modificó algún paso
                for idx, step in enumerate(scenario.steps):
                    if tc_info['steps'][idx]['actions'] != step.name:
                        tc_new_steps = TLBehave._create_scenario_steps_to_tl(scenario.steps)
                        break
                if tc_new_steps:
                    asd = client.updateTestCase(tc_info['testcase_id'], steps=tc_new_steps)
                    # print(asd)

            tc_id = client.getTestCaseIDByName(tc_name)[0]['id']

            if scenario.status.name == 'passed':
                scenario_status = 'p'
            else:
                scenario_status = 'f'

            image_url = ''
            steps = []
            for idx, step in enumerate(scenario.steps):
                notes = '{} seconds'.format(step.duration)

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
            git_rev_number = \
                str(subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD'])).split("'")[1].split('\\')[0]
            notes = 'git revision number: {}'.format(git_rev_number)
            execution = client.reportTCResult(tc_id, test_plan_id, scenario_status, context._root['new_build_id'],
                                              'MacOS',
                                              scenario.duration / 60, steps, notes=notes)
            print(execution)

            if scenario.status.name == 'failed':
                file = base64.b64encode(open(image_url, 'rb').read())
                upload_attachmeent = client.uploadExecutionAttachment(execution[0]['id'], 'img.png', 'image/png',
                                                                      file, 'Fail', 'Fail')
                # print(upload_attachmeent)

    def _create_scenario_steps_to_tl(steps):
        tc_steps = []
        for idx, step in enumerate(steps):
            tc_step = {'step_number': idx + 1,
                       'actions': step.name,
                       'expected_results': '',
                       'execution_type': 2}
            tc_steps.append(tc_step)
        return tc_steps

    # def create_new_test_suit(feature, client, test_project_id):
    #     ts = client.createTestSuite(test_project_id, feature.name)
    #     return ts

    def create_new_test_project(client, tp_name):
        tp_prefix = '{}{}'.format(random.choice(string.ascii_lowercase), random.choice(string.ascii_lowercase))
        ntp = client.createTestProject(tp_name, tp_prefix)
        return ntp
