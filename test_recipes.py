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

def test_recipe_title():
    ingredients = [Ingredient("Черемша", 200.0, "кг"), Ingredient("Стекловата", 67, "т"), Ingredient("Семга", 52, "кг"), Ingredient("Брдыщ", 42, "кг"), Ingredient("Тихо", 1488, "т"), Ingredient("Не спеша", 666, "т")]
    recipe = Recipe("СССР", ingredients)
    assert recipe.title == "СССР"

def test_recipe_len():
    ingredients = [Ingredient("Черемша", 200.0, "кг"), Ingredient("Стекловата", 67, "т"), Ingredient("Семга", 52, "кг"), Ingredient("Брдыщ", 42, "кг"), Ingredient("Тихо", 1488, "т"), Ingredient("Не спеша", 666, "т")]
    recipe = Recipe("СССР", ingredients)
    assert len(recipe.ingredients) == 6

def test_recipe_ingredients():
    ingredients = [Ingredient("Черемша", 200.0, "кг"), Ingredient("Стекловата", 67, "т"), Ingredient("Семга", 52, "кг"), Ingredient("Брдыщ", 42, "кг"), Ingredient("Тихо", 1488, "т"), Ingredient("Не спеша", 666, "т")]
    recipe = Recipe("СССР", ingredients)
    assert recipe.ingredients[0].name == "Черемша"

def test_recipe_creation_empty_ingredients():
    recipe = Recipe("Черемша")
    assert recipe.title == "Черемша"
    assert recipe.ingredients == []

def test_recipe_add_ingredient_new():
    recipe = Recipe("СССР")
    ingredients = [Ingredient("Черемша", 200.0, "кг"), Ingredient("Стекловата", 67, "т")]
    recipe.add_ingredient(Ingredient("Семга", 52, "кг"))
    assert len(recipe) == 1
    assert recipe.ingredients[0].name == "Семга"
    assert recipe.ingredients[0].quantity == 52

def test_recipe_add_ingredient_existing():
    recipe = Recipe("CCCР")
    recipe.add_ingredient(Ingredient("Черемша", 200, "кг"))
    recipe.add_ingredient(Ingredient("Черемша", 1288, "кг"))
    assert len(recipe) == 1
    assert recipe.ingredients[0].quantity == 1488

def test_recipe_is_valid_ratio():
    assert Recipe.is_valid_ratio(52) == True
    assert Recipe.is_valid_ratio(7.8) == True
    assert Recipe.is_valid_ratio(0) == False
    assert Recipe.is_valid_ratio(-228) == False
    assert Recipe.is_valid_ratio("six seven") == False

def test_recipe_len():
    recipe = Recipe("СССР")
    recipe.add_ingredient(Ingredient("Черемша", 200, "кг"))
    recipe.add_ingredient(Ingredient("Стекловата", 67, "т"))
    recipe.add_ingredient(Ingredient("Черемша", 200, "кг"))
    assert len(recipe) == 2

def test_recipe_str():
    recipe = Recipe("СССР", [Ingredient("Черемша", 200.0, "кг"), Ingredient("Стекловата", 67, "т"), Ingredient("Семга", 52, "кг"), Ingredient("Брдыщ", 42, "кг"), Ingredient("Тихо", 1488, "т"), Ingredient("Не спеша", 666, "т")])
    result = str(recipe)
    assert "Рецепт: СССР" in result
    assert "Черемша: 200.0 кг" in result

def test_recipe_scale_does_not_change_original():
    original = Recipe("СССР", [Ingredient("Черемша", 200.0, "кг")])
    original_quantity = original.ingredients[0].quantity
    scaled = original.scale(3)
    assert original.ingredients[0].quantity == original_quantity
    assert original.ingredients[0] is not scaled.ingredients[0] 

def test_recipe_add_ingredient_same_name_different_unit():
    recipe = Recipe("СССР")
    recipe.add_ingredient(Ingredient("Черемша", 6, "кг"))
    recipe.add_ingredient(Ingredient("Черемша", 7, "т"))
    assert len(recipe) == 2
    assert recipe.ingredients[0].name == "Черемша"
    assert recipe.ingredients[0].unit == "кг"
    assert recipe.ingredients[1].unit == "т"

def test_recipe_is_valid_ratio_edge_cases():
    assert Recipe.is_valid_ratio(0.00000000148822852426778) == True 
    assert Recipe.is_valid_ratio(True) == True 
    assert Recipe.is_valid_ratio(False) == False 
    assert Recipe.is_valid_ratio(None) == False  
    assert Recipe.is_valid_ratio([6,7]) == False 

def test_recipe_scale_with_float_ratio():
    recipe = Recipe("СССР", [Ingredient("Черемша", 200.0, "кг")])
    scaled = recipe.scale(0.5)  
    assert scaled.ingredients[0].quantity == 100.0

def test_recipe_add_ingredient_zero_quantity():
    with pytest.raises(ValueError):
        Ingredient("Черемша", 0, "кг")
        