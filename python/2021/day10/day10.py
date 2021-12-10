from python.download_input import get_input_content


def check_syntax(line):
    mapping = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }
    stack = []
    for char in line:
        # Add to stack if it is an opening char
        if char in '([{<':
            stack.append(char)
        # Check if it matches the last char in case of a closing one
        else:
            last = stack.pop()
            for opening, closing in (('(', ')'), ('[', ']'), ('{', '}'), ('<', '>')):
                if last == opening and char != closing:
                    # print(f'Expected {closing}, but found {char} instead')
                    return mapping[char]
    return 0


def first(data):
    score = 0
    for line in data:
        score += check_syntax(line)
    return score


def complete_line(line):
    mapping = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4,
    }
    stack = []
    for char in line:
        if char in '([{<':
            stack.append(char)
        else:
            last = stack.pop()
            for opening, closing in (('(', ')'), ('[', ']'), ('{', '}'), ('<', '>')):
                if last == opening and char != closing:
                    return

    if stack:
        score = 0
        for char in stack[::-1]:
            score *= 5
            score += mapping[char]
        return score


def second(data):
    scores = []
    for line in data:
        score = complete_line(line)
        if score:
            scores.append(score)
    scores.sort()
    return scores[len(scores)//2]


if __name__ == "__main__":
    content = get_input_content(__file__)

    print(f'Le résultat de la première partie est :\n{first(content)}')

    print(f'Le résultat de la deuxième partie est :\n{second(content)}')
