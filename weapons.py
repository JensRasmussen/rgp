from enum import Enum
from dice import Die, RedBlackDice
from random import random
from math import ceil

def create_weapon(weapon_type, attack_skill, damage_skill, crit_skill):
    weapon_type = weapon_type.upper() if weapon_type is not None else None
    if weapon_type == WeaponTypes.TINY:
        return Tiny(attack_skill, damage_skill, crit_skill)
    if weapon_type == WeaponTypes.SMALL:
        return Small(attack_skill, damage_skill, crit_skill)
    if weapon_type == WeaponTypes.MEDIUM:
        return Medium(attack_skill, damage_skill, crit_skill)
    else:
        return None

class WeaponTypes:
    TINY = "TINY"
    SMALL = "SMALL"
    MEDIUM = "MEDIUM"
    LARGE = "LARGE"
    SPEAR = "SPEAR"
    BOW = "BOW"

class Weapon:
    def __init__(self, attack_skill, damage_skill, crit_skill):
        self._attack_skill = attack_skill
        self._damage_skill = damage_skill
        self._crit_skill = crit_skill
    
    def attack(self):
        roll, attack_crit, attack_fumble = RedBlackDice(self._crit_skill).roll()
        return roll + self._attack_skill, attack_crit, attack_fumble

    def damage(self):
        return self._damage_roll() + self._damage_bonus()

    def crit_damage(self):
        return self.damage() + self._crit_bonus()

    def hands(self):
        return 1

    def _crit_bonus(self):
        # TODO: multiple dice if above d10
        dice_sides = (self._crit_skill // 2) * 2
        return int(dice_sides * random()) + 1

    def _damage_bonus(self):
        bonus = self._damage_skill // 2 if self.hands == 1 else self._damage_skill
        return bonus

    def _damage_roll(self):
        raise Exception('implement in inheritor')

class Tiny(Weapon):
    def __init__(self, attack_skill, damage_skill, crit_skill):
        super().__init__(attack_skill, damage_skill, crit_skill)        

    def _damage_roll(self):
        return Die(4).roll() + Die(4).roll()

class Small(Weapon):
    def __init__(self, attack_skill, damage_skill, crit_skill):
        super().__init__(attack_skill, damage_skill, crit_skill + 2)        

    def _damage_roll(self):
        return Die(6).roll() + Die(4).roll()

class Medium(Weapon):
    def __init__(self, attack_skill, damage_skill, crit_skill):
        super().__init__(attack_skill, damage_skill, crit_skill)        

    def _damage_roll(self):
        return Die(6).roll() + Die(6).roll()