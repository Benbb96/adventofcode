import re


steps = {}


def add_letters(letter, next):
    if letter in steps.keys():
        if 'children' in steps[letter]:
            steps[letter]['children'].append(next)
        else:
            steps[letter]['children'] = [next]
    else:
        steps[letter] = {'children': [next]}
    if next in steps.keys():
        if 'parent' in steps[next]:
            steps[next]['parent'].append(letter)
        else:
            steps[next]['parent'] = [letter]
    else:
        steps[next] = {'parent': [letter]}


def find_first_letters():
    first_letters = []
    for letter, value in steps.items():
        if not 'parent' in value:
            first_letters.append(letter)
    return first_letters


def first(input):
    answer = ''
    # Fill the steps
    for line in input:
        letter, next = [x.strip() for x in re.findall('( [A-Z] )', line)]
        add_letters(letter, next)

    available = find_first_letters()

    while len(answer) < len(steps.keys()):
        # Get alphabetically first letter available
        available.sort()
        next_letter = available.pop(0)
        answer += next_letter
        # If it has children, add the ones that are possible and not already available
        if 'children' in steps[next_letter]:
            for e in steps[next_letter]['children']:
                if e not in available:
                    parent = steps[e]['parent']
                    ok = True
                    for p in parent:
                        if p not in answer:
                            ok = False
                            break
                    if ok:
                        available.append(e)

    return answer


def second(order, nb):
    second = 0
    workers = [''] * nb
    answer = ''

    available = find_first_letters()
    i = 0
    for letter in available:
        workers[i] = letter
        i += 1

    print(workers)

    while len(answer) < 26:
        # TODO
        second +=1

    print(answer)
    return second


if __name__ == "__main__":
    with open('test.txt', 'r') as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    order = first(content)
    print("1. Le résultat est %s" % order)

    print("2. Le résultat est %s" % second(order, 2))
