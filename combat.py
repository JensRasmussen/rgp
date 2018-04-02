from fighter import Fighter

def fight(f1, f2, verbose=0):
    while True:
        initiative_f1 = f1.initiative()
        initiative_f2 = f2.initiative()
        if initiative_f1 != initiative_f2: break
    
    f1s_turn = initiative_f1 > initiative_f2
    if verbose > 0:
        if f1s_turn: print(f"{f1.name}: Won the initiative!")
        else: print(f"{f2.name}: Won the initiative!")

    while not f1.is_defeated and not f2.is_defeated:
        if f1s_turn:
            f2 = f1.attack(f2)
        else:
            f1 = f2.attack(f1)
        f1s_turn = not f1s_turn
    
    return f1, f2

def many_fights(f1, f2, count):
    wins_f1 = 0
    wins_f2 = 0
    for x in range(count):
        f1_after, f2_after = fight(f1, f2)
        if f1_after.is_defeated: wins_f2 += 1
        if f2_after.is_defeated: wins_f1 += 1
    return wins_f1, wins_f2

if __name__ == "__main__":
    import argparse
    import csv
    import itertools

    parser = argparse.ArgumentParser()
    parser.add_argument("fight_count", type=int)
    parser.add_argument("stats_file")

    args = parser.parse_args()
    with open(args.stats_file, newline='') as stats_file:
        stats_reader = csv.DictReader(stats_file)

        for (stats_f1, stats_f2) in itertools.combinations(stats_reader, 2):

            f1 = Fighter(stats_f1)
            f2 = Fighter(stats_f2)
            f1_wins, f2_wins = many_fights(f1, f2, args.fight_count)
            print(f"{f1.name} against {f2.name}: {f1_wins}/{f2_wins}: {100*f1_wins/(f1_wins+f2_wins)}%")
    

        
