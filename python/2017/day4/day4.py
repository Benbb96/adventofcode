test1 = 'aa bb cc dd ee'
test2 = 'aa bb cc dd aa'
test3 = 'aa bb cc dd aaa'

test4 = 'abcde fghij'
test5 = 'abcde xyz ecdab'
test6 = 'a ab abc abd abf abj'
test7 = 'iiii oiii ooii oooi oooo'
test8 = 'oiii ioii iioi iiio'


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
    sum_valid_passphrase = 0
    for passphrase in input:
        if is_valid(passphrase):
            sum_valid_passphrase += 1
    return sum_valid_passphrase


def no_anagram(passphrase):
    list_of_words = passphrase.split()
    list_of_words = [sorted(list(x)) for x in list_of_words]
    listCopy = list_of_words.copy()  # On créé une copie de la liste pour la comparer avec la première
    for word in list_of_words:
        listCopy.remove(word)
        if listCopy.__contains__(word):  # Si la liste contient encore le mot, c'est qu'il est en double
            return False
    return True



def second(input):
    sum_valid_passphrase = 0
    for passphrase in input:
        if no_anagram(passphrase):
            sum_valid_passphrase += 1
    return sum_valid_passphrase


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    # print(no_anagram(test8))

    print('1. Le nombre de passphrase valide est : ' + str(first(content)))
    print('2. Le nombre de passphrase valide est : ' + str(second(content)))