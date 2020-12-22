from collections import deque


def calc_total(cards):
    total = 0
    length = len(cards)
    for num in cards:
        total += length * num
        length -= 1
    return total


def first(player_1, player_2):
    while player_1 and player_2:
        first_1 = player_1.popleft()
        first_2 = player_2.popleft()
        if first_1 > first_2:
            player_1.append(first_1)
            player_1.append(first_2)
        else:
            player_2.append(first_2)
            player_2.append(first_1)

    return calc_total(player_1) if player_1 else calc_total(player_2)


class Game:
    def __init__(self, deque_1: deque, deque_2: deque):
        self.deque_1 = deque_1.copy()
        self.deque_2 = deque_2.copy()
        self.deque_1_history = []
        self.deque_2_history = []

    def play(self):
        while self.deque_1 and self.deque_2:
            # Check if deque for each player already was in the same order
            if self.deque_1 in self.deque_1_history or self.deque_2 in self.deque_2_history:
                return 1, self.deque_1
            # Add to history
            self.deque_1_history.append(self.deque_1.copy())
            self.deque_2_history.append(self.deque_2.copy())

            first_1 = self.deque_1.popleft()
            first_2 = self.deque_2.popleft()
            winner = None
            if len(self.deque_1) >= first_1 and len(self.deque_2) >= first_2:
                game = Game(
                    deque([self.deque_1[i] for i in range(first_1)]),
                    deque([self.deque_2[i] for i in range(first_2)])
                )
                winner, _ = game.play()

            if first_1 > first_2 and winner is None or winner == 1:
                self.deque_1.append(first_1)
                self.deque_1.append(first_2)
            else:
                self.deque_2.append(first_2)
                self.deque_2.append(first_1)
        return (1, self.deque_1) if self.deque_1 else (2, self.deque_2)


def second(player_1, player_2):
    game = Game(player_1, player_2)
    winner, cards = game.play()
    return calc_total(cards)


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    player_1 = deque()
    player_2 = deque()
    player_1_done = False
    for line in content:
        if ':' in line:
            continue
        if not player_1_done:
            if line == '':
                player_1_done = True
                continue
            player_1.append(int(line))
        else:
            player_2.append(int(line))

    print("1. Le résultat est %s" % first(player_1.copy(), player_2.copy()))

    print("2. Le résultat est %s" % second(player_1.copy(), player_2.copy()))
