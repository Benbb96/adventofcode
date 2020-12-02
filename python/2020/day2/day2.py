

def first(input):
    valid_passwords = 0
    for line in input:
        policy, letter, password = line.split()
        letter = letter[0]
        minimum, maximum = map(int, policy.split('-'))
        if minimum <= password.count(letter) <= maximum:
            valid_passwords += 1
    return valid_passwords


def second(input):
    valid_passwords = 0
    for line in input:
        policy, letter, password = line.split()
        letter = letter[0]
        first, second = map(int, policy.split('-'))
        if password[first - 1] != letter and password[second - 1] == letter or password[first - 1] == letter and password[second - 1] != letter:
            valid_passwords += 1
    return valid_passwords


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    print("1. Le résultat est %s" % first(content))

    print("2. Le résultat est %s" % second(content))
