"""
Cater Waiter
"""

from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
    """

    :param dish_name: str
    :param dish_ingredients: list
    :return: tuple of (dish_name, ingredient set)

    This function should return a `tuple` with the name of the dish as the first item,
    followed by the de-duped `set` of ingredients as the second item.
    """

    return (dish_name, set(dish_ingredients))


def check_drinks(drink_name, drink_ingredients):
    """

    :param drink_name: str
    :param drink_ingredients: list
    :return: str drink name + ("Mocktail" or "Cocktail")

    The function should return the name of the drink followed by "Mocktail" if the drink has
    no alcoholic ingredients, and drink name followed by "Cocktail" if the drink includes alcohol.
    """

    has_alcohol = any(map(lambda i: i in ALCOHOLS, drink_ingredients))

    if has_alcohol:
        return f'{drink_name} Cocktail'

    return f'{drink_name} Mocktail'


def categorize_dish(dish_name, dish_ingredients):
    """

    :param dish_name: str
    :param dish_ingredients: list
    :return: str "dish name: CATEGORY"

    This function should return a string with the `dish name: <CATEGORY>` (which meal category the dish belongs to).
    All dishes will "fit" into one of the categories imported from `sets_categories_data.py`
    (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).
    """

    category = 'UNKNOWN'

    is_vegan = len(dish_ingredients.difference(VEGAN)) == 0
    if is_vegan:
        category = 'VEGAN'

    is_vegetarian = len(dish_ingredients.difference(VEGETARIAN)) == 0
    if is_vegetarian:
        category = 'VEGETARIAN'

    is_paleo = len(dish_ingredients.difference(PALEO)) == 0
    if is_paleo:
        category = 'PALEO'

    is_keto = len(dish_ingredients.difference(KETO)) == 0
    if is_keto:
        category = 'KETO'

    is_omnivore = len(dish_ingredients.difference(OMNIVORE)) == 0
    if is_omnivore:
        category = 'OMNIVORE'

    return f'{dish_name}: {category}'


def tag_special_ingredients(dish):
    """

    :param dish: tuple of (str of dish name, list of dish ingredients)
    :return: tuple of (str of dish name, set of dish special ingredients)

    Return the dish name followed by the `set` of ingredients that require a special note on the dish description.
    For the purposes of this exercise, all allergens or special ingredients that need to be tracked are in the
    SPECIAL_INGREDIENTS constant imported from `sets_categories_data.py`.
    """

    (name, ingredients) = dish

    special_ingredients = set(ingredients).intersection(SPECIAL_INGREDIENTS)

    return (name, special_ingredients)


def compile_ingredients(dishes):
    """

    :param dishes: list of dish ingredient sets
    :return: set

    This function should return a `set` of all ingredients from all listed dishes.
    """

    return set.union(*dishes)


def separate_appetizers(dishes, appetizers):
    """

    :param dishes: list of dish names
    :param appetizers: list of appetizer names
    :return: list of dish names

    The function should return the list of dish names with appetizer names removed.
    Either list could contain duplicates and may require de-duping.
    """

    dish_set = set(dishes)
    appetizer_set = set(appetizers)

    dish_set_without_appetizers = dish_set.difference(appetizer_set)

    return list(dish_set_without_appetizers)


def singleton_ingredients(dishes, intersection):
    """

    :param intersection: constant - one of (VEGAN_INTERSECTION,VEGETARIAN_INTERSECTION,PALEO_INTERSECTION,
                                            KETO_INTERSECTION,OMNIVORE_INTERSECTION)
    :param dishes:  list of ingredient sets
    :return: set of singleton ingredients

    Each dish is represented by a `set` of its ingredients.
    Each `<CATEGORY>_INTERSECTION` is an `intersection` of all dishes in the category.
    The function should return a `set` of ingredients that only appear in a single dish.
    """

    unique_ingredients = set.union(*dishes)
    unique_ingredients.difference_update(intersection)

    return unique_ingredients
