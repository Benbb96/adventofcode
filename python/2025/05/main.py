from python.download_input import get_input_content


def first(data):
    ranges, ids = data.split('\n\n')
    ranges = ranges.split('\n')
    ranges = [tuple(map(int, r.split('-'))) for r in ranges]
    ids = map(int, ids.split('\n'))
    fresh_ids = set()
    for i in ids:
        for r in ranges:
            if r[0] <= i <= r[1]:
                print(i)
                fresh_ids.add(i)

    return len(fresh_ids)


def second(data):
    ranges = data.split('\n\n')[0]
    ranges = ranges.split('\n')
    ranges = [tuple(map(int, r.split('-'))) for r in ranges]

    i = 0
    while i < len(ranges):
        (i_start, i_end) = ranges[i]
        j = 0
        while j < len(ranges):
            if i == j:
                j += 1
                continue

            (j_start, j_end) = ranges[j]
            print((i_start, i_end), (j_start, j_end))
            if i_start <= j_start <= i_end or i_start <= j_end <= i_end or j_start <= i_start <= j_end or j_start <= i_end <= j_end:
                print('merge')
                ranges[i] = (min(i_start, j_start), max(i_end, j_end))
                print(ranges[i])
                (i_start, i_end) = ranges[i]
                del ranges[j]
                if j < i:
                    i -= 1
                j -= 1
            j += 1
        i += 1

    print()
    count = 0
    for r in ranges:
        print(r)
        count += r[1] - r[0] + 1

    return count


if __name__ == "__main__":
    content = get_input_content(__file__, False)
    test_input = '''3-5
10-14
16-20
12-18


1
5
8
11
17
32'''
    if test_input:
        content = test_input

    # print(f'Le résultat de la première partie est :\n{first(content)}')

    print(f'Le résultat de la deuxième partie est :\n{second(content)}')
    # 366759058207469 too high
