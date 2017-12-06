

def first(input):
    # Process
    return 1


def second(input):
    # Process
    return 1


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    print("1. Le résultat est " + str(first(content)))

    print("2. Le résultat est " + str(second(content)))