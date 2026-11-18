from selenium.webdriver.common.by import By


class CreateRecipeLocators:
    TITLE = (By.XPATH, "//form//label[div[normalize-space(.)='Название рецепта']]/input")
    DESCRIPTION = (By.CSS_SELECTOR, "form textarea")
    COOKING_TIME = (
        By.XPATH,
        "//form//label[div[normalize-space(.)='Время приготовления']]/input",
    )
    INGREDIENT_INPUT = (By.CSS_SELECTOR, 'form input[class*="ingredientsInput__"]')
    INGREDIENT_AMOUNT = (By.CSS_SELECTOR, 'form input[class*="ingredientsAmountValue__"]')
    ADD_INGREDIENT = (By.XPATH, "//form//div[normalize-space(.)='Добавить ингредиент']")
    ADDED_INGREDIENT = (By.CSS_SELECTOR, 'form span[class*="ingredientsAddedItemTitle__"]')
    IMAGE = (By.CSS_SELECTOR, 'form input[type="file"]')
    SUBMIT = (By.XPATH, "//form//button[normalize-space(.)='Создать рецепт']")

    @staticmethod
    def ingredient_option(name):
        return (
            By.XPATH,
            "//form//div[contains(@class, 'styles_ingredientsInputs__')]/div/div"
            f"[normalize-space(.)='{name}']",
        )
