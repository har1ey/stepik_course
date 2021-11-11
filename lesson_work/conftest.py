import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# https://docs.pytest.org/en/latest/example/simple.html?highlight=addoption


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Please set language, example 'es'")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
