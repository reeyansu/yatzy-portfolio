import random

class Yatzy:
    def __init__(self):
        self.dice = [random.randint(1, 6) for _ in range(5)]
        self.locked = [False] * 5

    def roll(self):
        for i in range(5):
            if not self.locked[i]:
                self.dice[i] = random.randint(1, 6)

    def ones(self):
        return self.dice.count(1) * 1

    def twos(self):
        return self.dice.count(2) * 2

    def threes(self):
        return self.dice.count(3) * 3

    def fours(self):
        return self.dice.count(4) * 4

    def fives(self):
        return self.dice.count(5) * 5

    def sixes(self):
        return self.dice.count(6) * 6
def chance(self):
    return sum(self.dice)
def three_of_a_kind(self):
    for i in set(self.dice):
        if self.dice.count(i) >= 3:
            return i * 3
    return 0
