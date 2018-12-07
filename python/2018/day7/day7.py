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


def first(input):
    answer = ''
    # Fill the steps
    for line in input:
        letter, next = [x.strip() for x in re.findall('( [A-Z] )', line)]
        add_letters(letter, next)

    print(steps)

    available = []

    # Find first letter
    possible_first = []
    for letter, value in steps.items():
        if not 'parent' in value:
            available.append(letter)

    while len(answer) < len(steps.keys()):
        # Get alphabetically first letter available
        available.sort()
        print('available :')
        print(available)
        next_letter = available.pop(0)
        answer += next_letter
        print(answer)
        # If it has children, add the ones that are possible and not already available
        if 'children' in steps[next_letter]:
            for e in steps[next_letter]['children']:
                if e not in available:
                    parent = steps[e]['parent']
                    print(parent)
                    ok = True
                    for p in parent:
                        print(p)
                        if p not in answer:
                            print('not ok')
                            ok = False
                            break
                    if ok:
                        available.append(e)

    return answer


def second(input):
    # Process
    return 2


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    print("1. Le résultat est %s" % first(content))

    print("2. Le résultat est %s" % second(content))
