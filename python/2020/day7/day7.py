import re

my_bag = 'shiny gold'


def first(input):
    all_bags = {}

    regex = re.compile('(\w+ \w+) bags?')

    for line in input:
        iterator = regex.finditer(line)
        first_iteration = True
        parent_bag = None
        for match in iterator:
            bag_color = match.group(1)
            if first_iteration:
                parent_bag = bag_color
                if bag_color not in all_bags.keys():
                    all_bags[bag_color] = {'parents': set()}
                first_iteration = False
            elif bag_color != 'no other':
                if bag_color not in all_bags.keys():
                    all_bags[bag_color] = {'parents': {parent_bag}}
                else:
                    all_bags[bag_color]['parents'].add(parent_bag)

    parents_of_shiny = set()
    parents = all_bags[my_bag]['parents']

    def add_to_parents(parents):
        for parent in parents:
            parents_of_shiny.add(parent)
            add_to_parents(all_bags[parent]['parents'])

    add_to_parents(parents)

    return len(parents_of_shiny)


def second(input):
    all_bags = {}

    parent_regex = re.compile('^(\w+ \w+)')
    children_regex = re.compile('(\d) (\w+ \w+)')

    for line in input:
        parent_color = parent_regex.search(line).group()
        if parent_color not in all_bags.keys():
            all_bags[parent_color] = {'children': {}}

        iterator = children_regex.finditer(line)
        for match in iterator:
            quantity = int(match.group(1))
            bag_color = match.group(2)
            if bag_color not in all_bags.keys():
                all_bags[bag_color] = {'children': {}}
            all_bags[parent_color]['children'][bag_color] = quantity

    def count_children(parent):
        total_count = 1
        for child, count in all_bags[parent]['children'].items():
            total_count += count * count_children(child)
        return total_count

    return count_children(my_bag) - 1  # Don't count my bag


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    print("1. Le résultat est %s" % first(content))

    print("2. Le résultat est %s" % second(content))
