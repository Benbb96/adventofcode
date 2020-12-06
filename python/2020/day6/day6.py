

def first(input):
    groups = []
    count = 0
    answered_questions = set()
    for line in input:

        if line == '':
            groups.append({
                'nb_person': count,
                'answered_questions': answered_questions
            })
            count = 0
            answered_questions = set()
            continue

        count += 1
        for letter in line:
            answered_questions.add(letter)
    # Add the last group
    groups.append({
        'nb_person': count,
        'answered_questions': answered_questions
    })

    return sum(len(group['answered_questions']) for group in groups)


def second(input):
    answered_by_everyone_in_group = 0
    people_in_group = []
    all_letters = set()
    for line in input:
        if line == '':
            for letter in all_letters:
                valid = True
                for person_letters in people_in_group:
                    if letter not in person_letters:
                        valid = False
                        break
                if valid:
                    answered_by_everyone_in_group += 1

            people_in_group = []
            all_letters = set()
            continue

        for letter in line:
            all_letters.add(letter)
        people_in_group.append(line)
    # Do it for the last group
    for letter in all_letters:
        valid = True
        for person_letters in people_in_group:
            if letter not in person_letters:
                valid = False
                break
        if valid:
            answered_by_everyone_in_group += 1

    return answered_by_everyone_in_group


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    print("1. Le résultat est %s" % first(content))

    print("2. Le résultat est %s" % second(content))
