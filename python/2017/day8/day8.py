variables = {}  # Dictionnaire pour stocker les variables et leurs valeurs


def condition_is_true(condition_variable, condition, condition_number):
    """
    Retourne vrai si la condition est vérifié
    :param condition_variable: la variable a vérifié
    :param condition: la condition à appliquer (égalité, supérieur, inférieur, etc.)
    :param condition_number: le nombre auquel comparé
    :return:
    """
    if condition == '==':
        return variables[condition_variable] == condition_number
    elif condition == '>':
        return variables[condition_variable] > condition_number
    elif condition == '>=':
        return variables[condition_variable] >= condition_number
    elif condition == '<':
        return variables[condition_variable] < condition_number
    elif condition == '<=':
        return variables[condition_variable] <= condition_number
    elif condition == '!=':
        return variables[condition_variable] != condition_number


def day8(input):
    max_in_process = 0
    max = 0

    #On initialise à 0 toutes les variables
    for line in input:
        variables[line.split()[0]] = 0

    for line in input:
        # On récupère toutes les infos en parsant la ligne
        variable = line.split()[0]
        action = line.split()[1]
        n = int(line.split()[2])
        condition_variable = line.split()[4]
        condition = line.split()[5]
        condition_number = int(line.split()[6])

        if condition_is_true(condition_variable, condition, condition_number):
            # Si la condition est vrai, on incrémente ou décremente la valeur en fonction
            if action == 'inc':
                variables[variable] += n
            elif action == 'dec':
                variables[variable] -= n
        # De plus, on vérifie si la valeur maximum pendant les calculs a été dépassé
            if variables[variable] > max_in_process:
                max_in_process = variables[variable]

    # On regarde quelle est le maximum à la fin du traitement
    for value in variables.values():
        if value > max:
            max = value

    return max, max_in_process


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    max1, max2 = day8(content)

    print("1. La valeur la plus haute à la fin des calculs est " + str(max1))
    print("2. La valeur la plus haute au cours du process est " + str(max2))