import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
from src.models.ingredient import Restriction


# Req 2
def test_dish():
    shrimp = Ingredient("camarão")
    salmon = Ingredient("salmão")
    heavy_cream = Ingredient("creme de leite")
    gorgonzola = Ingredient("queijo  gorgonzola")

    my_dish = Dish("sea_food", 37.50)
    your_dish = Dish("heavy_cheese", 16.35)
    your_dish_again = Dish("heavy_cheese", 16.35)

    my_dish.add_ingredient_dependency(shrimp, 12)
    my_dish.add_ingredient_dependency(salmon, 4)

    your_dish.add_ingredient_dependency(heavy_cream, 1)
    your_dish.add_ingredient_dependency(gorgonzola, 3)

    your_dish_again.add_ingredient_dependency(heavy_cream, 1)
    your_dish_again.add_ingredient_dependency(gorgonzola, 3)

    assert my_dish.__eq__(your_dish) is False
    assert your_dish.__eq__(your_dish_again) is True
    assert your_dish.__hash__() == your_dish_again.__hash__()

    assert my_dish.__hash__() != your_dish.__hash__()

    assert my_dish.name == "sea_food"

    assert my_dish.__repr__() == "Dish('sea_food', R$37.50)"

    assert my_dish.get_restrictions() == {
        Restriction.ANIMAL_MEAT,
        Restriction.SEAFOOD,
        Restriction.ANIMAL_DERIVED,
    }
    assert my_dish.get_ingredients() == {
        Ingredient("salmão"),
        Ingredient("camarão"),
    }

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("sea_food", "37.50")

    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("sea_food", -37.50)
