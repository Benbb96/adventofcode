from python.download_input import get_input_content


def first(data):
    count = 0
    for line in data:
        unique_patterns, digit_outputs = line.split(' | ')
        for digit_output in digit_outputs.split():
            if len(digit_output) not in (5, 6):
                count += 1

    return count


def second(data):
    possible_mapping_by_letter = {letter: [] for letter in 'abcdef'}
    print(possible_mapping_by_letter)
    mapping_by_digit = {digit: None for digit in range(10)}
    print(mapping_by_digit)
    count = 0
    for line in data:
        print(line)
        unique_patterns, digit_outputs = line.split(' | ')
        for digit_output in digit_outputs.split():
            if len(digit_output) == 2 and not mapping_by_digit[1]:
                # Digit = 1
                mapping_by_digit[1] = set(list(digit_output))
            elif len(digit_output) == 3 and not mapping_by_digit[7]:
                # Digit = 7
                mapping_by_digit[7] = set(list(digit_output))
            elif len(digit_output) == 4 and not mapping_by_digit[4]:
                # Digit = 4
                mapping_by_digit[4] = set(list(digit_output))
            elif len(digit_output) == 7 and not mapping_by_digit[8]:
                # Digit = 8
                mapping_by_digit[8] = set(list(digit_output))
    print(mapping_by_digit)

    return count


if __name__ == "__main__":
    content = get_input_content(__file__)
    test_input = '''be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce'''
    if test_input:
        content = test_input.split('\n')

    print(f'Le résultat de la première partie est :\n{first(content)}')

    print(f'Le résultat de la deuxième partie est :\n{second(content)}')
