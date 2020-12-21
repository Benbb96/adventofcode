class Ingredient:
    def __init__(self, name: str):
        self.name = name
        self.allergen = None
        self.possible_allergens = set()

    def __str__(self) -> str:
        return self.name

    def add_possible_allergen(self, allergen):
        if not self.allergen:
            self.possible_allergens.add(allergen)


class Allergen:
    def __init__(self, name: str):
        self.name = name
        self.ingredient = None
        self.possible_ingredients = set()

    def __str__(self) -> str:
        return self.name

    def add_possible_ingredients(self, ingredients):
        if not self.ingredient:
            for ingredient in self.possible_ingredients:
                if ingredient not in ingredients:
                    self.possible_ingredients.remove(ingredient)
                    ingredient.possible_allergens.remove(self)
            for ingredient in ingredients:
                self.possible_ingredients.add(ingredient)
