test1 = 'aa bb cc dd ee'
test2 = 'aa bb cc dd aa'
test3 = 'aa bb cc dd aaa'
test4 = 'teuvzf tdtwoi dpkjk cwgjk ccur lgmqv jpjdkk efrnw uloqn dpkjk lwloeph'


def is_valid(passphrase):
    list_of_words = passphrase.split()
    list = list_of_words.copy()  # On créé une copie de la liste pour la comparer avec la première
    for word in list_of_words:
        list.remove(word)
        if list.__contains__(word):  # Si la liste contient encore le mot, c'est qu'il est en double
            # print('Le mot en double est ' + word + '\n')
            return False
    return True


def first(input):
    with open(input, 'r') as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    sum_valid_passphrase = 0
    for passphrase in content:
        if is_valid(passphrase):
            sum_valid_passphrase += 1

    return sum_valid_passphrase


if __name__ == "__main__":
    #print(is_valid(test4))
    print('1. Le nombre de passphrase valide est : ' + str(first('input.txt')))