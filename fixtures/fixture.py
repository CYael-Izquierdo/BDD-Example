from behave import fixture, use_fixture
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from features.steps.constants import Constants


@fixture
def browser_chrome(context, timeout=30):

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=1920x1080')
    context.browser = webdriver.Chrome(executable_path=Constants.CHROMEDRIVER_PATH,
                                       chrome_options=options)

    # context.browser = webdriver.Chrome(executable_path=Constants.CHROMEDRIVER_PATH)
    yield context.browser
    # -- CLEANUP-FIXTURE PART:
    context.browser.quit()


@fixture
def browser_safari(context, timeout=30):
    # -- HINT: @behave.fixture is similar to @contextlib.contextmanager
    context.browser = webdriver.Safari('/usr/bin/safaridriver')
    yield context.browser
    # -- CLEANUP-FIXTURE PART:
    context.browser.quit()


@fixture
def browser_firefox(context, timeout=30):
    # -- HINT: @behave.fixture is similar to @contextlib.contextmanager
    context.browser = webdriver.Firefox(executable_path='/Users/cizquierdo/PycharmProjects/BBDExample/geckodriver')
    yield context.browser
    # -- CLEANUP-FIXTURE PART:
    context.browser.quit()
