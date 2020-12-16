

def first(input):
    my_ticket = False
    rules_done = False
    possible_valid_values = set()
    invalid_values = []
    for line in input:
        if not rules_done:
            if line == '':
                rules_done = True
            else:
                rule, conditions = line.split(': ')
                # Add possible valid values by iterating through the range
                for range_ in conditions.split(' or '):
                    range_ = [int(x) for x in range_.split('-')]
                    for x in range(range_[0], range_[1] + 1):
                        possible_valid_values.add(x)
        elif not my_ticket:
            if ',' not in line:
                continue
            my_ticket = True
        else:
            if ',' not in line:
                continue
            for value in map(int, line.split(',')):
                if value not in possible_valid_values:
                    invalid_values.append(value)
    return sum(invalid_values)


def second(input):
    rules = {}
    my_ticket = None
    nearby_tickets = []
    rules_done = False
    possible_valid_values = set()
    invalid_values = []
    for line in input:
        if not rules_done:
            if line == '':
                rules_done = True
            else:
                rule, conditions = line.split(': ')
                rules[rule] = conditions.split(' or ')
                for range_ in rules[rule]:
                    range_ = [int(x) for x in range_.split('-')]
                    for x in range(range_[0], range_[1] + 1):
                        possible_valid_values.add(x)
        elif not my_ticket:
            if ',' not in line:
                continue
            my_ticket = [int(x) for x in line.split(',')]
        else:
            if ',' not in line:
                continue
            current_ticket = [int(x) for x in line.split(',')]
            ok = True
            for value in current_ticket:
                if value not in possible_valid_values:
                    invalid_values.append(value)
                    ok = False
            if ok:
                nearby_tickets.append(current_ticket)
    nearby_tickets.append(my_ticket)

    # For each rule, try each fields of each tickets to know if it would fit at this position
    rules_possible_positions = {rule: [] for rule in rules.keys()}
    for rule, conditions in rules.items():
        range_1 = [int(x) for x in conditions[0].split('-')]
        range_2 = [int(x) for x in conditions[1].split('-')]
        for i in range(len(rules)):
            ok = True
            for ticket in nearby_tickets:
                field = ticket[i]
                if (range_1[0] > field or field > range_1[1]) and (range_2[0] > field or field > range_2[1]):
                    ok = False
                    break
            if ok:
                rules_possible_positions[rule].append(i)

    # Order the rule starting by rule which has only one possible position then two and so on
    ordered_rules = [''] * len(rules)
    used_position = []
    for rule, positions in sorted(rules_possible_positions.items(), key=lambda x: len(x[1])):
        diff = [i for i in positions + used_position if i not in positions or i not in used_position]
        pos = diff[0]
        ordered_rules[pos] = rule
        used_position.append(pos)

    # Do the product of each of my ticket fields that starts with 'departure'
    product = 1
    for i, rule in enumerate(ordered_rules):
        if rule.startswith('departure'):
            product *= my_ticket[i]

    return product


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    print("1. Le résultat est %s" % first(content))

    print("2. Le résultat est %s" % second(content))
