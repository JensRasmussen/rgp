import random

class Die:
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return int(random.random() * self.sides)

class RedBlackDice:
    def __init__(self, crit_skill):
        self._crit_bonus = (crit_skill*2) // 3

    def roll(self):
        red = Die(6).roll()
        black = Die(6).roll()
        red_req = 6 - self._crit_bonus // 6
        black_req = 6 - self._crit_bonus % 6
        is_crit = red > red_req or (red == red_req and black >= black_req) 
        is_fumble = red == 1 and black == 1
        return red + black, is_crit, is_fumble
