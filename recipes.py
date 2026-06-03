class Ingredient:
    def __init__(self, name: str, quantity: float, unit: str):
        self.name = name
        self.quantity = float(quantity)
    @property
    def quantity(self):
        return self.quantity
    @quantity.setter
    def quantity(self, value):
        value = float(value)
        if value <= 0:
            raise ValueError("Количество должно быть положительным")
        self.quantity = value
    def __str__(self):
        return f"{self.name}:{self.quantity} {self.unit}"
    def __repr__(self):
        return f"Ingredient('{self.name}',{self.quantity},'{self.unit}')"
    def __eq__(self, other):
        if not isinstance(other, Ingredient):
            return False
        return self.name==other.name and self.unit==other.unit

class Recipe:
    def __init__(self, title, ingredients=None):
        self.title = title
        if ingredients is None:
            self.ingredients = []
        else:
            self.ingredients = ingredients
    def add_ingredient(self, ingredient):
        found = False
        for i in range(len(self.ingredients)):
            existing = self.ingredients[i]
            if existing.name == ingredient.name and existing.unit == ingredient.unit:
                existing.quantity+= ingredient.quantity
                found = True
                break
        if not found:
            self.ingredients.append(ingredient)
    @staticmethod
    def is_valid_ratio(ratio):
        if type(ratio) == int or type(ratio) == float:
            if ratio>0:
                return True
        return False
    def scale(self, ratio):
        if self.is_valid_ratio(ratio) == False:
            raise ValueError("Коэффициент масштабирования должен быть положительным числом")
        new_ingredients = []
        for ing in self.ingredients:
            new_quantity = ing.quantity*ratio
            new_ing = Ingredient(ing.name, new_quantity, ing.unit)
            new_ingredients.append(new_ing)
        return Recipe(self.title, new_ingredients)
    def __len__(self):
        count = 0
        for ing in self.ingredients:
            count+= 1
        return count
    def __str__(self):
        result = "Рецепт: " + self.title
        for ing in self.ingredients:
            result = result + "\n  - " + str(ing)
        return result