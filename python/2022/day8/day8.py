from python.download_input import get_input_content


def first(data):
    visible_trees = 0
    r = 0
    while r < len(data):
        c = 0
        while c < len(data[r]):
            if r == 0 or c == 0 or r == len(data) - 1 or c == len(data[r]) - 1:
                visible_trees += 1
            else:
                visible = False
                if all(data[r][i] < data[r][c] for i in range(c)):
                    visible = True
                elif all(data[i][c] < data[r][c] for i in range(r)):
                    visible = True
                elif all(data[r][i] < data[r][c] for i in range(len(data[r]) - 1, c, -1)):
                    visible = True
                elif all(data[i][c] < data[r][c] for i in range(len(data) - 1, r, -1)):
                    visible = True
                if visible:
                    visible_trees += 1
            c += 1
        r += 1

    return visible_trees


def second(data):
    scenic_scores = []
    r = 1
    while r < len(data) - 1:
        c = 1
        while c < len(data[r]) - 1:
            scenic_score = 1
            # to left
            visible_trees = 0
            for i in range(c - 1, -1, -1):
                visible_trees += 1
                if data[r][i] >= data[r][c]:
                    break
            scenic_score *= visible_trees

            # to up
            visible_trees = 0
            for i in range(r - 1, -1, -1):
                visible_trees += 1
                if data[i][c] >= data[r][c]:
                    break
            scenic_score *= visible_trees

            # to rigth
            visible_trees = 0
            for i in range(c + 1, len(data[r])):
                visible_trees += 1
                if data[r][i] >= data[r][c]:
                    break
            scenic_score *= visible_trees

            # to down
            visible_trees = 0
            for i in range(r + 1, len(data)):
                visible_trees += 1
                if data[i][c] >= data[r][c]:
                    break
            scenic_score *= visible_trees

            scenic_scores.append(scenic_score)
            c += 1
        r += 1

    return max(scenic_scores)


if __name__ == "__main__":
    content = get_input_content(__file__)
    test_input = '''30373
25512
65332
33549
35390'''
    # if test_input:
    #     content = test_input.split('\n')

    grid = [list(line) for line in content]

    print(f'Le résultat de la première partie est :\n{first(grid)}')

    print(f'Le résultat de la deuxième partie est :\n{second(grid)}')
