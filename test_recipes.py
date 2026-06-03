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

def test_recipe_len_after_add_ingredient():
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

def test_shoppinglist_get_list_same_ingredient_same_recipe():
    sl = ShoppingList()
    recipe = Recipe("СССР")
    recipe.add_ingredient(Ingredient("Черемша", 200, "кг"))
    recipe.add_ingredient(Ingredient("Черемша", 1288, "кг"))
    sl.add_recipe(recipe, 1)
    result = sl.get_list()
    assert len(result) == 1
    assert result[0].name == "Черемша"
    assert result[0].quantity == 1488

def test_shoppinglist_remove_recipe_multiple_entries():
    sl = ShoppingList()
    recipe = Recipe("СССР", [Ingredient("Черемша", 200, "кг")])
    sl.add_recipe(recipe, 1)
    sl.add_recipe(recipe, 2)
    assert len(sl._items) == 2
    sl.remove_recipe("СССР")
    assert len(sl._items) == 0

def test_shoppinglist_get_list_sorting_order():
    sl = ShoppingList()
    sl.add_recipe(Recipe("Рецепт1", [Ingredient("Черемша", 200, "кг")]), 1)
    sl.add_recipe(Recipe("Рецепт2", [Ingredient("Стекловата", 67, "т")]), 1)
    sl.add_recipe(Recipe("Рецепт3", [Ingredient("Семга", 52, "кг")]), 1)
    sl.add_recipe(Recipe("Рецепт4", [Ingredient("Брдыщ", 42, "кг")]), 1)
    sl.add_recipe(Recipe("Рецепт5", [Ingredient("Тихо", 1488, "т")]), 1)
    sl.add_recipe(Recipe("Рецепт6", [Ingredient("Не спеша", 666, "т")]), 1)
    result = sl.get_list()
    names = [ing.name for ing in result]
    assert names == sorted(names)

def test_shoppinglist_get_list_no_duplicates_after_aggregation():
    sl = ShoppingList()
    r1 = Recipe("Рецепт1", [Ingredient("Черемша", 200, "кг")])
    r2 = Recipe("Рецепт2", [Ingredient("Черемша", 300, "кг")])
    r3 = Recipe("Рецепт3", [Ingredient("Черемша", 400, "кг")])
    sl.add_recipe(r1, 1)
    sl.add_recipe(r2, 1)
    sl.add_recipe(r3, 1)
    result = sl.get_list()
    черемша_count = 0
    for ing in result:
        if ing.name == "Черемша":
            черемша_count += 1
    assert черемша_count == 1
    assert result[0].quantity == 900

def test_shoppinglist_remove_recipe_nonexistent():
    sl = ShoppingList()
    recipe = Recipe("СССР", [Ingredient("Черемша", 200, "кг")])
    sl.add_recipe(recipe, 1)
    sl.remove_recipe("Брдыщ")
    assert len(sl._items) == 1
    assert sl._items[0][0].name == "Черемша"

def test_shoppinglist_get_list_empty():
    sl = ShoppingList()
    result = sl.get_list()
    assert result == []

def test_shoppinglist_add_recipe_with_dietary():
    sl = ShoppingList()
    dietary = DietaryRecipe("СССР", "Черемшовая диета", [Ingredient("Черемша", 200, "кг")])
    sl.add_recipe(dietary, 2)
    assert len(sl._items) == 1
    assert sl._items[0][0].quantity == 400
    assert sl._items[0][1] == "СССР"