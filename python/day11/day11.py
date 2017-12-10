

def first(input):
    for c in input:
        print(c)


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        # content = f.readlines()
        content = f.readline()
    content = [x.strip() for x in content]

    first(content)