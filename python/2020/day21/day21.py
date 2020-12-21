from models import Ingredient, Allergen


def parse(line):
    part1, part2 = line.split(' (contains ')
    ingredients = part1.split()
    allergens = part2[:-1].split(', ')
    return ingredients, allergens


def first(input):
    all_ingredients = {}
    all_allergens = {}
    for line in input:
        ingredients, allergens = parse(line)
        line_ingredients = []
        for ingredient in ingredients:
            ingredient = all_ingredients.setdefault(ingredient, Ingredient(ingredient))
            line_ingredients.append(ingredient)
            for allergen in allergens:
                allergen = all_allergens.setdefault(allergen, Allergen(allergen))
                ingredient.add_possible_allergen(allergen)
        for allergen in allergens:
            allergen.add_possible_ingredients(line_ingredients)
    print(f'{all_ingredients=}')
    print(f'{all_allergens=}')

    return 1


def second(input):
    # Process
    return 2


if __name__ == "__main__":
    with open('test.txt', 'r') as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    print("1. Le résultat est %s" % first(content))

    print("2. Le résultat est %s" % second(content))
