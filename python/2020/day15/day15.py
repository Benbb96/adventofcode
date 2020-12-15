from time import time


def first(input, limit):
    turn = len(input) + 1
    last_pos = {n: i+1 for i, n in enumerate(input)}
    last = input[-1]
    while turn <= limit:
        pos_before_last = last_pos.get(last, turn-1)
        next_number = turn-1 - pos_before_last
        last_pos[last] = turn - 1
        last = next_number
        turn += 1
    return last


if __name__ == "__main__":
    # test = [0, 3, 6]
    content = [0, 14, 1, 3, 7, 9]
    start = time()

    print("1. Le résultat est %s" % first(content, 2020))

    print("2. Le résultat est %s" % first(content, 30000000))
