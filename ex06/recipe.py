import string
import sys


cookbook = {
    "Sandwich": {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 10
    },
    "Cake": {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60
    },
    "Salad": {
        "ingredients": ["avocado", "arugula", "spinach", "tomatoes"],
        "meal": "lunch",
        "prep_time": 15
    }
}


def print_recipe(name):
    print("Recipe for {}:".format(name))
    print("Ingredients list: {}".format(cookbook[name]["ingredients"]))
    print("To be eaten for {}".format(cookbook[name]["meal"]))
    print("Takes {} minutes of cooking".format(cookbook[name]["prep_time"]))
    return


def delete_recipe(name):
    if name in cookbook:
        cookbook.pop(name)
        print("{} deleted from cookbook".format(name))
    else:
        print("Recipe doesn't exist")
    return


def add_recipe(name, ingredients, meal, prep_time):
    cookbook[name] = dict(ingredients=ingredients, meal=meal, prep_time=prep_time)
    return


def print_all_recipe():
    i = 1
    for x in cookbook:
        print("{} : {}".format(i, x))
        i += 1
    return


def cookbook_prog():
    ingredients = []
    name = ""
    meal = ""
    prep_time = 0
    print("Please select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")
    for line in sys.stdin:
        if line == '1\n':
            print("Name of the new recipe:")
            for line2 in sys.stdin:
                name = line2
                break
            print("Ingredients of the new recipe (one by one, press Enter when finished):")
            for line3 in sys.stdin:
                if line3 == '\n':
                    break
                ingredients.append(line3)
            print("Type of meal:")
            for line4 in sys.stdin:
                meal = line4
                break
            print("Preparation time:")
            for line5 in sys.stdin:
                prep_time = int(line5)
                break
            add_recipe(name, ingredients, meal, prep_time)
            print("Recipe added to cookbook !")
        elif line == '2\n':
            print("Name of the recipe you want to delete:")
            for line6 in sys.stdin:
                name = line6
                break
            delete_recipe(name)
        elif line == '3\n':
            print("Name of the recipe you want to print:")
            for line7 in sys.stdin:
                name = line7
                break
            print_recipe(name)
        elif line == '4\n':
            print_all_recipe()
        elif line == '5\n':
            print("Good bye !")
            break
        else:
            print("This option does not exist, please type the corresponding number.\nTo exit, enter 5.")
    return


cookbook_prog()
