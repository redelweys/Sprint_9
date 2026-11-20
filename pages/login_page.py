import allure
from selenium.webdriver.support import expected_conditions as EC

from locators.login_locators import LoginLocators
from pages.base_page import BasePage
from urls import LOGIN_URL


class LoginPage(BasePage):
    @allure.step("Открыть страницу входа")
    def open(self):
        self.open_url(LOGIN_URL)

    @allure.step("Перейти к регистрации по ссылке в меню")
    def click_signup(self):
        self.click(LoginLocators.SIGNUP_LINK)

    def fill_form(self, user):
        with allure.step("Заполнить форму входа"):
            self.fill(LoginLocators.EMAIL, user.username)
            self.fill(LoginLocators.PASSWORD, user.password)

    @allure.step("Отправить форму входа")
    def submit(self):
        self.click(LoginLocators.SUBMIT)

    @allure.step("Дождаться перехода на страницу входа")
    def is_open(self):
        return self.wait.until(EC.url_to_be(LOGIN_URL))

    @allure.step("Дождаться отображения формы входа")
    def is_form_visible(self):
        form = self.wait.until(EC.visibility_of_element_located(LoginLocators.FORM))
        return form.is_displayed()
