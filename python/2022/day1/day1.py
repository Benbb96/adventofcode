from python.download_input import get_input_content


def get_calories(data: list[str]) -> list:
    elves_calories = []
    elf = 0
    for line in data:
        if line == '':
            elves_calories.append(elf)
            elf = 0
        else:
            elf += int(line)
    # Sort with maximum first
    return sorted(elves_calories, reverse=True)


if __name__ == "__main__":
    content = get_input_content(__file__)
    test_input = ''''''
    if test_input:
        content = test_input.split('\n')

    calories = get_calories(content)

    print(f'Le résultat de la première partie est :\n{calories[0]}')

    print(f'Le résultat de la deuxième partie est :\n{sum(calories[:3])}')
