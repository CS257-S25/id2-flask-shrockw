'''
This file is the command line interface for the project.
'''
from ProductionCode.random_recipe import get_random_recipes
from ProductionCode.data import get_data



def usage_statement():
    ''' Display the usage statements for the command line interface. '''

    print("Usage: python cl.py --search --include_ingredients " \
    "<ingredients> --omit_ingredients <ingredients>")
    print("<ingredients> should be a comma-separated list " \
           "of ingredients enclosed in quotes.")
    print("or python cl.py --random <number>")
    print("or python cl.py --help")
    print("--search or --s: Search for a specific recipe.")
    print("--random or --r: Get a random recipe.")
    print("--help or --h: Display help message.")


def print_recipes(recipes):
    ''' Print the recipes found line by line. '''
    for recipe in recipes:
        print(recipe)


def random_cl(num):
    ''' Get a random n number of recipes.'''
    recipe_data = get_data("recipe_data.csv", "Data")
    recipe_data = recipe_data[1:]
    random_recipes = get_random_recipes(recipe_data, num)
    output = ""
    for recipe in random_recipes:
        output += f"{recipe[0]}: {recipe[2]}\n"
    return output
