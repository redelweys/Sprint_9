from selenium.webdriver.common.by import By


class RecipeCardLocators:
    CARD = (By.CSS_SELECTOR, 'div:has(> img[class*="single-card__image__"])')
    TITLE = (By.CSS_SELECTOR, 'h1[class*="single-card__title__"]')
