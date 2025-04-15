import random

class Die:
    def __init__(self):
        self.value = random.randint(1, 6)
        self.locked = False

    def roll(self):
        if not self.locked:
            self.value = random.randint(1, 6)

    def __repr__(self):
        return f"{'[LOCKED]' if self.locked else ''} {self.value}"


class Yatzy:
    def __init__(self):
        self.dice = [Die() for _ in range(5)]
        self.roll()

    def roll(self):
        for die in self.dice:
            die.roll()

    def lock_die(self, index):
        if 0 <= index < len(self.dice):
            self.dice[index].locked = True
                
    def unlock_die(self, index):
        if 0 <= index < len(self.dice):
            self.dice[index].locked = False


    def unlock_all(self):
        for die in self.dice:
            die.locked = False

    def get_dice_values(self):
        return [die.value for die in self.dice]

    def chance(self):
        return sum(self.get_dice_values())

    def ones(self): return self.get_dice_values().count(1) * 1
    def twos(self): return self.get_dice_values().count(2) * 2
    def threes(self): return self.get_dice_values().count(3) * 3
    def fours(self): return self.get_dice_values().count(4) * 4
    def fives(self): return self.get_dice_values().count(5) * 5
    def sixes(self): return self.get_dice_values().count(6) * 6

    def one_pair(self):
        values = self.get_dice_values()
        for num in range(6, 0, -1):
            if values.count(num) >= 2:
                return num * 2
        return 0

    def two_pairs(self):
        values = self.get_dice_values()
        pairs = []
        for num in range(6, 0, -1):
            if values.count(num) >= 2:
                pairs.append(num)
                if len(pairs) == 2:
                    return sum(p * 2 for p in pairs)
        return 0

    def three_alike(self):
        values = self.get_dice_values()
        for num in range(6, 0, -1):
            if values.count(num) >= 3:
                return num * 3
        return 0

    def four_alike(self):
        values = self.get_dice_values()
        for num in range(6, 0, -1):
            if values.count(num) >= 4:
                return num * 4
        return 0

    def small(self):
        return 15 if sorted(self.get_dice_values()) == [1, 2, 3, 4, 5] else 0

    def large(self):
        return 20 if sorted(self.get_dice_values()) == [2, 3, 4, 5, 6] else 0

    def full_house(self):
        values = self.get_dice_values()
        unique = set(values)
        if len(unique) == 2:
            a, b = unique
            if values.count(a) in [2, 3] and values.count(b) in [2, 3]:
                return sum(values)
        return 0

    def yatzy(self):
        values = self.get_dice_values()
        return 50 if values.count(values[0]) == 5 else 0
