from collections import Counter

from python.download_input import get_input_content


def first(polymer, data):
    pair_insertions = {}
    for line in data:
        ab, c = line.split(' -> ')
        pair_insertions[ab] = c

    for step in range(10):
        next_polymer = ''
        prev = ''
        for c in polymer:
            if prev and (prev + c) in pair_insertions:
                next_polymer += prev + pair_insertions[prev + c]
            prev = c
        polymer = next_polymer + polymer[-1]

    counter = Counter(polymer)

    return max(counter.values()) - min(counter.values())


def second(polymer, data):
    pair_insertions = {}
    for line in data:
        ab, c = line.split(' -> ')
        pair_insertions[ab] = c

    pair_counter = Counter()
    i = 0
    while i < len(polymer):
        if i > 0:
            pair_counter[polymer[i-1]+polymer[i]] += 1
        i += 1

    for step in range(40):
        next_pair_counter = Counter()
        for pair, count in pair_counter.items():
            if pair in pair_insertions:
                next_pair_counter[pair[0] + pair_insertions[pair]] += count
                next_pair_counter[pair_insertions[pair] + pair[1]] += count
        pair_counter = next_pair_counter

    counter = Counter()
    for pair, count in pair_counter.items():
        counter[pair[0]] += count
    # Add last letter
    counter[polymer[-1]] += 1

    return max(counter.values()) - min(counter.values())


if __name__ == "__main__":
    content = get_input_content(__file__)

    template = content[0]
    content = content[2:]

    print(f'Le résultat de la première partie est :\n{first(template, content)}')

    print(f'Le résultat de la deuxième partie est :\n{second(template, content)}')
