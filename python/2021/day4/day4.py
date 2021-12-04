import re

from python.download_input import get_input_content


def get_board_col(board, i):
    col = []
    for row in board:
        col.append(row[i])
    return col


def first(numbers, boards):
    for number in numbers:
        for board in boards:
            for row in board:
                for i, cell in enumerate(row):
                    if cell[0] == number:
                        row[i] = (number, True)
                        # Check if row is complete
                        if all(c[1] for c in row) or all(c[1] for c in get_board_col(board, i)):
                            somme = 0
                            for row in board:
                                for cell in row:
                                    if not cell[1]:
                                        somme += cell[0]
                            return somme * number


def second(numbers, boards):
    winning_boards = []
    for number in numbers:
        for board in boards:
            if board not in winning_boards:
                for row in board:
                    for i, cell in enumerate(row):
                        if cell[0] == number:
                            row[i] = (number, True)
                            # Check if row is complete
                            if all(c[1] for c in row) or all(c[1] for c in get_board_col(board, i)):
                                winning_boards.append(board)
                                if len(winning_boards) == len(boards):
                                    somme = 0
                                    for row in board:
                                        for cell in row:
                                            if not cell[1]:
                                                somme += cell[0]
                                    return somme * number


if __name__ == "__main__":
    content = get_input_content(__file__)

    numbers = list(map(int, content[0].split(',')))
    boards = []
    current_board = -1
    i = 0
    for line in content[1:]:
        if line == '':
            i = 0
            current_board += 1
            continue
        row = list(map(int, re.findall(r'\d\d?', line)))
        if i == 0:
            boards.append([[(r, False) for r in row]])
        else:
            boards[current_board].append([(r, False) for r in row])
        i += 1

    print(f'Le résultat de la première partie est :\n{first(numbers, boards)}')

    print(f'Le résultat de la deuxième partie est :\n{second(numbers, boards)}')
