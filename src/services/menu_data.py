import csv

from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.file = source_path
        self.dishes = set()
        self.load_dishes()

    def load_dishes(self):
        with open(self.file, "r") as file:
            menu_reader = csv.reader(file, delimiter=",", quotechar='"')
            _, *data = menu_reader

            dishes_dict = {}

            for row in data:
                name = row[0]
                price = row[1]
                recipe_amount = row[3]

                ingredient = Ingredient(row[2])

                if name not in dishes_dict:
                    dishes_dict[name] = Dish(name, float(price))

                dish = dishes_dict[name]
                dish.add_ingredient_dependency(ingredient, int(recipe_amount))

            self.dishes = set(dishes_dict.values())
        return self.dishes
