from selenium.webdriver.common.by import By


class LoginLocators:
    SIGNUP_LINK = (By.LINK_TEXT, "Создать аккаунт")
    EMAIL = (By.NAME, "email")
    PASSWORD = (By.NAME, "password")
    SUBMIT = (By.CSS_SELECTOR, "form button")
    FORM = (
        By.CSS_SELECTOR,
        'form:has(input[name="email"]):has(input[name="password"])',
    )
