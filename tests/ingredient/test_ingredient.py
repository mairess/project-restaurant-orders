from src.models.ingredient import Ingredient  # noqa: F401, E261, E501
from src.models.ingredient import Restriction


# Req 1
def test_ingredient():
    chicken = Ingredient("frango")
    shrimp = Ingredient("camarão")
    other_shrimp = Ingredient("camarão")

    assert chicken.__eq__(shrimp) is False

    assert shrimp.name == "camarão"

    assert shrimp.__hash__() != chicken.__hash__()

    assert shrimp.__hash__() == other_shrimp.__hash__()

    assert shrimp.__eq__(other_shrimp) is True

    assert shrimp.__repr__() == "Ingredient('camarão')"

    assert shrimp.restrictions == {
        Restriction.ANIMAL_MEAT,
        Restriction.SEAFOOD,
        Restriction.ANIMAL_DERIVED,
    }
