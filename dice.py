import random

class Die:
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return int(random.random() * self.sides) + 1

class RedBlackDice:
    def __init__(self, crit_skill, verbose=1):
        self._crit_bonus = (crit_skill*2) // 3
        self._verbose = verbose

    def roll(self):
        red = Die(6).roll()
        black = Die(6).roll()
        red_req = 6 - self._crit_bonus // 6
        black_req = 6 - self._crit_bonus % 6
        is_crit = red > red_req or (red == red_req and black >= black_req) 
        is_fumble = red == 1 and black == 1
        if (self._verbose > 0):
            print(f"rolled: {red}/{black} (red/black)")
        return red + black, is_crit, is_fumble
