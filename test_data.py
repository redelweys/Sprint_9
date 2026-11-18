from dataclasses import dataclass
from pathlib import Path
from uuid import uuid4


APP_DIR = Path(__file__).resolve().parent


@dataclass(frozen=True)
class UserData:
    first_name: str
    last_name: str
    username: str
    email: str
    password: str


def make_user():
    username = f"qa_{uuid4().hex[:12]}"
    return UserData(
        first_name="Анна",
        last_name="Тестова",
        username=username,
        email=f"{username}@example.com",
        password=f"Qa!{uuid4().hex}",
    )


@dataclass(frozen=True)
class RecipeData:
    title: str
    description: str
    cooking_time: str
    ingredient_name: str
    ingredient_amount: str
    image_path: Path


def make_recipe():
    return RecipeData(
        title=f"Морковный салат QA {uuid4().hex[:10]}",
        description="Натереть морковь и перемешать.",
        cooking_time="10",
        ingredient_name="морковь",
        ingredient_amount="150",
        image_path=APP_DIR / "assets" / "recipe.png",
    )
