import allure


class TestCreateRecipe:
    @allure.title("Новый рецепт открывается в карточке с заданным названием")
    def test_create_recipe_opens_card(
        self, logged_in_recipes_page, create_recipe_page, recipe_card_page, new_recipe
    ):
        logged_in_recipes_page.click_create_recipe()
        create_recipe_page.fill_fields(
            new_recipe.title, new_recipe.description, new_recipe.cooking_time
        )
        create_recipe_page.add_ingredient(
            new_recipe.ingredient_name, new_recipe.ingredient_amount
        )
        create_recipe_page.upload_image(new_recipe.image_path)
        create_recipe_page.submit()

        assert recipe_card_page.is_card_visible()
        assert recipe_card_page.get_title() == new_recipe.title
