from behave import given, when, then
from pageObject import pageObject as Po
import names
from features.steps.constants import Constants


@given('I am logged in redmine home page')
def step_impl(context):
    context.browser.get(Constants.BASE_URL)
    loguot_po = Po.BaseLogoutPO(context.browser)
    login_po = loguot_po.goto_login()
    login_po.login('user', 'bitnami1')


@when('I go to create new project')
def step_impl(context):
    base_login_po = Po.BaseLoginPO(context.browser)
    projects_po = base_login_po.goto_projects()
    projects_po.goto_new_project()


@when('I enter the new project data without modules')
def step_impl(context):
    new_project_po = Po.NewProjectPO(context.browser)
    context.project_name = names.get_full_name()
    new_project_po.create_new_project_without_modules(context.project_name)


@then('I should see a successful creation alert')
def step_impl(context):
    project_settings_po = Po.ProjectSettingsPO(context.browser)
    assert ('Successful creation.' == project_settings_po.get_flash_notice_text())


@then('I should be able to find the created project in Projects tab')
def step_impl(context):
    base_login_po = Po.BaseLoginPO(context.browser)
    projects_po = base_login_po.goto_projects()
    project = projects_po.find_project_by_name(context.project_name)
    assert (context.project_name in project.text)
