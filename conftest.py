import pytest
from selenium import webdriver
from selenium.webdriver.remote.file_detector import LocalFileDetector

from pages.create_recipe_page import CreateRecipePage
from pages.login_page import LoginPage
from pages.recipe_card_page import RecipeCardPage
from pages.recipes_page import RecipesPage
from pages.signup_page import SignupPage
from test_data import make_recipe, make_user


def pytest_addoption(parser):
    parser.addoption(
        "--selenoid-uri",
        help="URL удалённого WebDriver, например http://selenoid:4444/wd/hub",
    )


@pytest.fixture
def browser(pytestconfig):
    selenoid_uri = pytestconfig.getoption("--selenoid-uri")
    if selenoid_uri:
        driver = webdriver.Remote(
            command_executor=selenoid_uri,
            options=webdriver.ChromeOptions(),
            file_detector=LocalFileDetector(),
        )
    else:
        driver = webdriver.Chrome()
    try:
        yield driver
    finally:
        driver.quit()


@pytest.fixture
def login_page(browser):
    page = LoginPage(browser)
    page.open()
    return page


@pytest.fixture
def signup_page(browser):
    return SignupPage(browser)


@pytest.fixture
def new_user():
    return make_user()


@pytest.fixture
def registered_user(login_page, signup_page, new_user):
    login_page.click_signup()
    signup_page.fill_form(new_user)
    signup_page.submit()
    login_page.is_open()
    return new_user


@pytest.fixture
def guest_recipes_page(browser, registered_user):
    page = RecipesPage(browser)
    page.open()
    return page


@pytest.fixture
def logged_in_recipes_page(guest_recipes_page, login_page, registered_user):
    guest_recipes_page.click_login()
    login_page.fill_form(registered_user)
    login_page.submit()
    guest_recipes_page.is_logout_visible()
    return guest_recipes_page


@pytest.fixture
def create_recipe_page(browser):
    return CreateRecipePage(browser)


@pytest.fixture
def recipe_card_page(browser):
    return RecipeCardPage(browser)


@pytest.fixture
def new_recipe():
    return make_recipe()
