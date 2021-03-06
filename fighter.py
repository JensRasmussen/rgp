from dice import Die, RedBlackDice
from weapons import create_weapon

class Fighter:
    def __init__(self, stats, verbose=0):
        self._stats = stats
        self._verbose = verbose
        self._weapon, self._weapon_offhand = self._create_weapon(stats)
        self._initiative_skill = int(stats["initiative_skill"])
        self._soak = int(stats["soak"])
        self._hitpoints = int(stats["hitpoints"])
        self._crit_skill = int(stats["crit_skill"])
        self._defence_skill = int(stats["defence_skill"])
        self._injuries = 0

        self.name = stats["name"]
        self.is_defeated = False

    def initiative(self):
        roll, is_crit, is_fumble = RedBlackDice(self._crit_skill).roll()
        initiative_level = roll + self._initiative_skill

        if is_crit:
            self._speak("Ha! Critted initiative!", initiative_level)
        elif is_fumble:
            self._speak("Shit! Fumbled initiative!", initiative_level)
        else:
            self._speak("Initiative", initiative_level)

        return initiative_level, is_crit, is_fumble

    def attack(self, opponent):
        opponent_after = self._attack_weapon(self._weapon, opponent)
        if self._weapon_offhand is None: return opponent_after

        return self._attack_weapon(self._weapon_offhand, opponent_after)

    def _attack_weapon(self, weapon, opponent):
        opponent_after = opponent
        attack_level, attack_crit, attack_fumble = weapon.attack()        
        if not attack_fumble and not opponent._avoids_attack(attack_level, attack_crit):
            damage = weapon.crit_damage() if attack_crit else weapon.damage()
            opponent_after = opponent._injure(damage)
        if attack_crit:
            self._speak("Ha! Critted attack!", attack_level)
        elif attack_fumble:
            self._speak("Shit! Fumbled attack!", attack_level)
        return opponent_after

    def _avoids_attack(self, attack_level, attack_crit):
        roll, defence_crit, defence_fumble = RedBlackDice(self._crit_skill).roll()
        defence_bonus = roll + self._defence_skill
        is_avoided = defence_crit or (not defence_fumble and not attack_crit and defence_bonus >= attack_level)

        if defence_crit:
            self._speak("Ha! Critted defence!", defence_bonus)
        elif defence_fumble:
            self._speak("Shit! Fumbled defence!", defence_bonus)
        elif is_avoided:
            self._speak("Dodged that one!", defence_bonus)
        else:
            self._speak("Got hit!", defence_bonus)

        return is_avoided
    
    def _injure(self, damage):
        injury = max(damage - self._soak, 0)
        if self._verbose > 0: self._speak(f"Injured: {injury}({damage})")
        new_status = Fighter(self._stats, self._verbose)
        new_status._injuries = self._injuries + injury
        if injury >= self._hitpoints or new_status._injuries > new_status._hitpoints:
            self._speak("Argh! Defeated!")
            new_status.is_defeated = True
        return new_status

    def _create_weapon(self, stats):
        weapon_type = stats["weapon_type"]
        attack_skill = int(stats["attack_skill"])
        damage_skill = int(stats["damage_skill"])
        crit_skill = int(stats["crit_skill"])
        weapon_type_offhand = stats["weapon_type_offhand"]
        attack_skill_offhand = attack_skill + int(stats["attack_penalty_offhand"])

        weapon = create_weapon(weapon_type, attack_skill, damage_skill, crit_skill)
        weapon_offhand = create_weapon(weapon_type_offhand, attack_skill_offhand, damage_skill, crit_skill)

        return weapon, weapon_offhand

    def _speak(self, msg, roll = None):
        if self._verbose > 0:
            if roll is None:
                print(f"{self.name}: {msg}")
            else:
                print(f"{self.name}: {msg} ({roll})")



    

    
        