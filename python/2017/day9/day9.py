test1 = '{}'
test2 = '{{{}}}'
test3 = '{{},{}}'
test4 = '{{{},{},{{}}}}'
test5 = '{<a>,<a>,<a>,<a>}'
test6 = '{{<ab>},{<ab>},{<ab>},{<ab>}}'
test7 = '{{<!!>},{<!!>},{<!!>},{<!!>}'
test8 = '{{<a!>},{<a!>},{<a!>},{<ab>}}'
test9 = '{<{o"i!a,<{i<a>}'

def day9(s):
    score = 0
    level = 0
    garbage = False
    non_canceled_char = 0
    i = 0
    while i < len(s):
        if s[i] == '!':
            i +=2
            continue
        elif not garbage and s[i] == '<':
            garbage = True
        elif garbage and s[i] == '<':
            non_canceled_char += 1
        elif s[i] == '>':
            garbage = False
        elif not garbage and s[i] == '{':
            level += 1
            score += level
        elif not garbage and s[i] == '}':
            level -= 1
        elif garbage:
            non_canceled_char +=1
            print(s[i])
        i += 1
    return score, non_canceled_char


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        content = f.readline()
    content = [x.strip() for x in content]

    score, non_canceled_char = day9(content)

    print("1. Le score  est " + str(score))

    print("2. Le nombre de mot non effacés est " + str(non_canceled_char))