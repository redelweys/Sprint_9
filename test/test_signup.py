import allure


class TestSignup:
    @allure.title("После создания аккаунта открывается форма входа")
    def test_signup_opens_login_form(self, login_page, signup_page, new_user):
        login_page.click_signup()
        signup_page.fill_form(new_user)
        signup_page.submit()

        assert login_page.is_open()
        assert login_page.is_form_visible()
