from selenium.webdriver.common.by import By


class RecipesLocators:
    LOGIN_LINK = (By.LINK_TEXT, "Войти")
    CREATE_RECIPE_LINK = (By.LINK_TEXT, "Создать рецепт")
    LOGOUT_CONTROL = (
        By.XPATH,
        "//*[self::a or self::button][normalize-space(.)='Выход']",
    )
