import allure
from selenium.webdriver.support import expected_conditions as EC

from locators.recipe_card_locators import RecipeCardLocators as Locators
from pages.base_page import BasePage


class RecipeCardPage(BasePage):
    @allure.step("Дождаться отображения карточки рецепта")
    def is_card_visible(self):
        card = self.wait.until(EC.visibility_of_element_located(Locators.CARD))
        return card.is_displayed()

    @allure.step("Получить название из карточки рецепта")
    def get_title(self):
        title = self.wait.until(EC.visibility_of_element_located(Locators.TITLE))
        return title.text
