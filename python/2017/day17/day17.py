

def first(step):
    buffer = [0]
    pos = 0
    for value in range(1, 2018):
        # print('value ' + str(value))
        pos = (pos + step) % len(buffer)
        buffer.insert(pos +1, value)
        pos = pos +1
        #print(buffer)
    return buffer[pos+1]


def second(step):
    # Pas besoin de stocker l'ordre des numéros pour cette partie
    size = 1
    pos = 0
    stop = 0
    for value in range(50000000):
        to_ins = value + 1
        new = (pos + step) % size
        new += 1
        if new == 1:
            # Dès qu'on tombe sur la valeur 1, juste après 0 (qui se trouve toujours au début)
            stop = to_ins # On remet à jour la valeur qui va stopper le spinlock
        pos = new
        size += 1
    return stop


if __name__ == "__main__":

    print("1. Le valeur juste après 2017 est " + str(first(394)))

    print("2. Le valeur juste après 0 est " + str(second(394)))
