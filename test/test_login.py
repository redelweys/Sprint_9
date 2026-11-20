import allure


class TestLogin:
    @allure.title("После входа открываются рецепты и появляется «Выход»")
    def test_login_opens_recipes_page(
        self, guest_recipes_page, login_page, registered_user
    ):
        guest_recipes_page.click_login()
        login_page.fill_form(registered_user)
        login_page.submit()

        assert guest_recipes_page.is_open()
        assert guest_recipes_page.is_logout_visible()
