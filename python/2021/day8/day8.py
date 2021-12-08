from python.download_input import get_input_content


def first(data):
    count = 0
    for line in data:
        unique_patterns, digit_outputs = line.split(' | ')
        for digit_output in digit_outputs.split():
            if len(digit_output) not in (5, 6):
                count += 1

    return count


def difference_between_two_digit(a, b):
    return list(set(a).difference(set(b)))


def second(data):
    count = 0
    for line in data:
        print(line)
        possible_mapping_by_letter = {letter: [] for letter in 'abcdefg'}
        mapping_by_digit = {digit: None for digit in range(10)}
        unique_patterns, digit_outputs = line.split(' | ')
        five_segments = []
        six_segments = []
        for unique_pattern in unique_patterns.split():
            # Sort letters
            unique_pattern = ''.join(sorted(unique_pattern))
            if len(unique_pattern) == 2 and not mapping_by_digit[1]:
                # Digit = 1
                mapping_by_digit[1] = unique_pattern
            elif len(unique_pattern) == 3 and not mapping_by_digit[7]:
                # Digit = 7
                mapping_by_digit[7] = unique_pattern
            elif len(unique_pattern) == 4 and not mapping_by_digit[4]:
                # Digit = 4
                mapping_by_digit[4] = unique_pattern
            elif len(unique_pattern) == 5:
                # Digits 2, 3, 5
                five_segments.append(unique_pattern)
            elif len(unique_pattern) == 6:
                # Digits 0, 6, 9
                six_segments.append(unique_pattern)
            elif len(unique_pattern) == 7 and not mapping_by_digit[8]:
                # Digit = 8
                mapping_by_digit[8] = unique_pattern

        # Add possible for c and f
        for letter in mapping_by_digit[1]:
            possible_mapping_by_letter['c'].append(letter)
            possible_mapping_by_letter['f'].append(letter)
        # Find a
        a = difference_between_two_digit(mapping_by_digit[7], mapping_by_digit[1])[0]
        possible_mapping_by_letter['a'] = [a]
        # Add possible for b and d
        b_and_d = difference_between_two_digit(mapping_by_digit[4], mapping_by_digit[1])
        for letter in b_and_d:
            possible_mapping_by_letter['b'].append(letter)
            possible_mapping_by_letter['d'].append(letter)
        # Find 3
        for five_segment in five_segments:
            if mapping_by_digit[1][0] in five_segment and mapping_by_digit[1][1]:
                mapping_by_digit[3] = five_segment
                break
        five_segments.remove(mapping_by_digit[3])
        # Find g
        d_and_g = difference_between_two_digit(mapping_by_digit[3], mapping_by_digit[7])
        g = difference_between_two_digit(d_and_g, mapping_by_digit[4])[0]
        possible_mapping_by_letter['g'] = [g]
        d = difference_between_two_digit(d_and_g, g)[0]
        possible_mapping_by_letter['d'] = [d]
        # Find 0
        for six_segment in six_segments:
            if possible_mapping_by_letter['d'][0] not in six_segment:
                mapping_by_digit[0] = six_segment
                break
        print(mapping_by_digit)
        print(possible_mapping_by_letter)
        six_segments.remove(mapping_by_digit[0])
        # TODO...

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
