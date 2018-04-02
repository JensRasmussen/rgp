import unittest
from weapons import WeaponTypes 
from fighter import Fighter
from combat import fight, many_fights

class TestCombat(unittest.TestCase):

    def test_fight_verbose(self):
        stats = {
            "name": "Conan",
            "weapon_type": WeaponTypes.TINY,
            "attack_skill": 10,
            "defence_skill": 10,
            "damage_skill": 8,
            "crit_skill": 4,
            "weapon_type_offhand": WeaponTypes.TINY,
            "attack_penalty_offhand": 0,
            "initiative_skill": 8,
            "hitpoints": 28,
            "soak": 4,
        }
        fighter1 = Fighter(stats, verbose=1)
        fighter2 = Fighter(stats, verbose=1)

        f1_after, f2_after = fight(fighter1, fighter2)

        self.assertNotEqual(f1_after.is_defeated, f2_after.is_defeated)

    def test_kato_someone(self):    
        stats_f1 = {
            "name": "Kato",
            "weapon_type": WeaponTypes.TINY,
            "attack_skill": 10,
            "defence_skill": 10,
            "damage_skill": 6,
            "crit_skill": 5,
            "weapon_type_offhand": WeaponTypes.TINY,
            "attack_penalty_offhand": 0,
            "initiative_skill": 5,
            "hitpoints": 28,
            "soak": 4,
        }
        stats_f2 = {
            "name": "Someone",
            "weapon_type": WeaponTypes.MEDIUM,
            "attack_skill": 10,
            "defence_skill": 10,
            "damage_skill": 10,
            "crit_skill": 5,
            "weapon_type_offhand": None,
            "attack_penalty_offhand": 0,
            "initiative_skill": 3,
            "hitpoints": 32,
            "soak": 4,
        }
        fighter1 = Fighter(stats_f1, verbose=1)
        fighter2 = Fighter(stats_f2, verbose=1)

        self.assertEqual(False, fighter1.is_defeated)
        self.assertEqual(False, fighter2.is_defeated)

        wins_f1, wins_f2 = many_fights(fighter1, fighter2, 1)

        self.assertAlmostEqual(0.5, wins_f1 / (wins_f1 + wins_f2), 1)

    def test_equal_fighters(self):    
        stats = {
            "name": "John Doe",
            "weapon_type": WeaponTypes.MEDIUM,
            "attack_skill": 10,
            "defence_skill": 10,
            "damage_skill": 6,
            "crit_skill": 3,
            "weapon_type_offhand": None,
            "attack_penalty_offhand": 0,
            "initiative_skill": 3,
            "hitpoints": 32,
            "soak": 4,
        }
        fighter1 = Fighter(stats)
        fighter2 = Fighter(stats)

        self.assertEqual(False, fighter1.is_defeated)
        self.assertEqual(False, fighter2.is_defeated)

        wins_f1, wins_f2 = many_fights(fighter1, fighter2, 1000)

        self.assertAlmostEqual(0.5, wins_f1 / (wins_f1 + wins_f2), 1)



