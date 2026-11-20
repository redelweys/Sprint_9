import allure

from locators.signup_locators import SignupLocators
from pages.base_page import BasePage


class SignupPage(BasePage):
    def fill_form(self, user):
        with allure.step("Заполнить форму регистрации"):
            self.fill(SignupLocators.FIRST_NAME, user.first_name)
            self.fill(SignupLocators.LAST_NAME, user.last_name)
            self.fill(SignupLocators.USERNAME, user.username)
            self.fill(SignupLocators.EMAIL, user.email)
            self.fill(SignupLocators.PASSWORD, user.password)

    @allure.step("Отправить форму регистрации")
    def submit(self):
        self.click(SignupLocators.SUBMIT)
