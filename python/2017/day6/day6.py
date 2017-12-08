# A refaire sur Processing !!!

test = '0\t2\t7\t0'


def first(input):
    history = [input]  # Tableau pour stocker les stocks de blocks des banques mémoires après chaque étape
    memory_banks = input.split('\t')  #Le tableau contenant chaque banque mémoire avec leur stock
    nb_memory_banks = len(memory_banks)  # Le nombre de banque
    memory_banks = list(map(int, memory_banks))  # On map les stocks pour que ce soit des entiers
    cycle = False  # Variable de fin de boucle
    redistribution = 0  # Compteur de redistribution
    while cycle == False:
        redistribution += 1
        # print('Redistribution n°' + str(redistribution))
        # print(memory_banks)
        max_blocks = 0
        # Recherche de la banque avec le plus de block
        for id, memory_bank in enumerate(memory_banks):
            if memory_bank > max_blocks:
                max_blocks = memory_bank
                id_max = id
        memory_banks[id_max] = 0
        current_id = id_max + 1 % nb_memory_banks
        # Redistribution des blocks
        for block in range(max_blocks):
            memory_banks[current_id % nb_memory_banks] += 1
            current_id += 1
        # Vérification si on a pas déjà été dans cet état là
        if history.__contains__('\t'.join(str(e) for e in memory_banks)):
            # Oui, donc on arrête les redistributions
            cycle = True
        else:
            # Non, donc on ajoute l'image de l'état à l'historique
            history.append('\t'.join(str(e) for e in memory_banks))

    # print(str(memory_banks) + " est déjà apparu. C'est un cycle !")
    pattern = '\t'.join(str(e) for e in memory_banks)  # Le pattern à rechercher dans la partie 2
    return redistribution, history, pattern




def second(history, pattern_to_find):
    count = 0  # Le compteur qui se déclenche dès qu'on a trouvé le pattern
    for i, pattern in enumerate(history):
        if count > 0 or pattern == pattern_to_find:
            count += 1
    return count


if __name__ == "__main__":
    # content = test
    content = open('input.txt').readline()
    redistribution, history, memory_banks = first(content)
    print("1. Le résultat est " + str(redistribution))
    print("2. Le résultat est " + str(second(history, memory_banks)))