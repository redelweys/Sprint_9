import allure
from selenium.webdriver.support import expected_conditions as EC

from locators.recipes_locators import RecipesLocators
from pages.base_page import BasePage
from urls import RECIPES_URL


class RecipesPage(BasePage):
    @allure.step("Открыть страницу рецептов")
    def open(self):
        self.driver.get(RECIPES_URL)

    @allure.step("Нажать «Войти» в меню")
    def click_login(self):
        self.click(RecipesLocators.LOGIN_LINK)

    @allure.step("Перейти на вкладку «Создать рецепт»")
    def click_create_recipe(self):
        self.click(RecipesLocators.CREATE_RECIPE_LINK)

    @allure.step("Дождаться перехода на страницу рецептов")
    def is_open(self):
        return self.wait.until(EC.url_to_be(RECIPES_URL))

    @allure.step("Дождаться отображения элемента «Выход»")
    def is_logout_visible(self):
        control = self.wait.until(
            EC.visibility_of_element_located(RecipesLocators.LOGOUT_CONTROL)
        )
        return control.is_displayed()
