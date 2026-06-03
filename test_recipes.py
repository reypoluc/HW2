import pytest
from recipes import Ingredient, Recipe, ShoppingList, DietaryRecipe

def test_ingredient_name():
    ingredient = Ingredient("Черемша", 200.0, "кг")
    assert ingredient.name == "Черемша"
def test_ingredient_quantity():
    ingredient = Ingredient("Черемша", 200.0, "кг")
    assert ingredient.quantity == 200.0
def test_ingredient_unit():
    ingredient = Ingredient("Черемша", 200.0, "кг")
    assert ingredient.unit == "кг"

def test_ingredient_str():
    ingredient = Ingredient("Черемша", 200.0, "кг")
    assert str(ingredient) == "Черемша: 200.0 кг"

def test_ingredient_repr():
    ingredient = Ingredient("Черемша", 200.0, "кг")
    assert repr(ingredient) == "Ingredient('Черемша', 200.0, 'кг')"

def test_ingredient_eq():
    ingredient1 = Ingredient("Черемша", 200.0, "кг")
    ingredient2 = Ingredient("Груз", 200.0, "кг")
    ingredient3 = Ingredient("Черемша", 67.0, "кг")
    ingredient4 = Ingredient("Черемша", 67.0, "т")
    assert ingredient1 != ingredient2
    assert ingredient1 == ingredient3
    assert ingredient1 != ingredient4

def test_ingredient_quantity_positive():
    ingredient = Ingredient("Черемша", 200.0, "кг")
    with pytest.raises(ValueError):
        ingredient.quantity = -52