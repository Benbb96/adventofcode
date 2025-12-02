from download_input import get_input_content


def check_invalid_id(id: str, part_1: bool = True):
    half = len(id) // 2

    if part_1:
        return id[:half] == id[half:]
    
    # part 2
    for i in range(half):
        if len(id) % (i + 1) == 0:
            sequence = id[:i + 1]
            if id.count(sequence) == len(id) // len(sequence):
                return True

    return False

def resolve(data: str, part_1: bool = True):
    invalid_ids_sum = 0
    ranges = data.split(',')
    for r in ranges:
        [start, end] = map(int, r.split('-'))
        for i in range(start, end + 1):
            if check_invalid_id(str(i), part_1):
                invalid_ids_sum += i

    return invalid_ids_sum


if __name__ == "__main__":
    content = get_input_content(__file__, False)
    test_input = '''11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'''
    # if test_input:
    #     content = test_input

    print(f'Le résultat de la première partie est :\n{resolve(content)}')

    print(f'Le résultat de la deuxième partie est :\n{resolve(content, False)}')
