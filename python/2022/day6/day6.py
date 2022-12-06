from python.download_input import get_input_content


def get_start_of_packet(msg: str, length: int) -> int:
    i = length
    while i < len(msg):
        if len(set(msg[i-length:i])) == length:
            return i
        i += 1
    raise ValueError(f'Message does not contain a sequence of {length} different characters.')


if __name__ == "__main__":
    content = get_input_content(__file__, split_by_lines=False)

    print(f'Le résultat de la première partie est :\n{get_start_of_packet(content, 4)}')

    print(f'Le résultat de la deuxième partie est :\n{get_start_of_packet(content, 14)}')
