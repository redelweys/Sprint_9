import allure
from selenium.webdriver.support import expected_conditions as EC

from locators.create_recipe_locators import CreateRecipeLocators as Locators
from pages.base_page import BasePage


class CreateRecipePage(BasePage):
    @allure.step("Заполнить название, описание и время приготовления")
    def fill_fields(self, title, description, cooking_time):
        self.fill(Locators.TITLE, title)
        self.fill(Locators.DESCRIPTION, description)
        self.fill(Locators.COOKING_TIME, cooking_time)

    @allure.step("Выбрать ингредиент из списка и добавить его в рецепт")
    def add_ingredient(self, name, amount):
        self.fill(Locators.INGREDIENT_INPUT, name)
        self.click(Locators.ingredient_option(name))
        self.fill(Locators.INGREDIENT_AMOUNT, amount)
        self.click(Locators.ADD_INGREDIENT)
        self.wait.until(
            EC.text_to_be_present_in_element(Locators.ADDED_INGREDIENT, name)
        )

    @allure.step("Загрузить изображение рецепта")
    def upload_image(self, image_path):
        file_input = self.wait.until(EC.presence_of_element_located(Locators.IMAGE))
        file_input.send_keys(str(image_path))

    @allure.step("Отправить форму создания рецепта")
    def submit(self):
        self.click(Locators.SUBMIT)
