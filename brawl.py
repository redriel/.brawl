# .brawl
# a lighweight fighting simulator
# by @redriel
# v1.1

import fighter
import recruiter
import random
ROUND_LIMIT = 14

print(".brawl started")

recruiter = recruiter.Recruiter('roster.json')
fighter_one = recruiter.select(input("Chose fighter 1: "))
fighter_two = recruiter.select(input("Chose fighter 2: "))

fighter_one.announce()
fighter_two.announce()

# fastest fighter starts first
if (fighter_one.nimble > fighter_two.nimble):
    attack_fighter = fighter_one
    defense_fighter = fighter_two
else:
    attack_fighter = fighter_two
    defense_fighter = fighter_one

round_count = 0
print('+---------+')
print(f"| Round {round_count+1} |")
print('+---------+')

# main cycle of the match
while (attack_fighter.stamina > 0 and defense_fighter.stamina > 0 and round_count <= ROUND_LIMIT):

    # a tecnique occurs based on rng
    tecnique_chance = random.randint(0, 99)
    tecnique_scored = False
    if (attack_fighter.books >= tecnique_chance):
        attack = attack_fighter.tecnique
        tecnique_scored = True
    else:
        attack = attack_fighter.punchforce
    
    # dodges and damage resistance are rng-based as well
    elusion_chance = random.randint(0, 99)
    resistance_chance = random.randint(0,99)
    elusion_scored = False
    if (defense_fighter.nimble >= elusion_chance):
        attack = 0
        elusion_scored = True
    if (resistance_chance >= 49):
        attack -= defense_fighter.tough
    if (attack < 0):
        attack = 0
    defense_fighter.stamina -= attack

    # logs with info on the fight
    if (tecnique_scored == True):
        print(f"{attack_fighter.name} throws a <<{attack_fighter.tecnique_name}>> for {attack} dmg!")
    else:
        print(f"{attack_fighter.name} throws a punch to {defense_fighter.name} for {attack} dmg.")

    # if a tecnique occurs, the match could be over
    ko_occurred = False
    if (tecnique_scored == True and elusion_scored == False):
        ko_chance = random.randint(0, 99)
        if (defense_fighter.guts < ko_chance):
            defense_fighter.stamina = 0
            print(f"   -> {defense_fighter.name} is knocked out!")
            ko_occurred = True
            break

    # logs with further info on dodges and resistance
    if (elusion_scored == True):
        print(f"   -> {defense_fighter.name} dodged at the last second!")
    if(resistance_chance >= 49 and elusion_scored == False):
        print(f"   -> {defense_fighter.name} withstanded the blow!")
    
    # swapping attacking e defendig fighters and carrying on with the match
    attack_fighter, defense_fighter = defense_fighter, attack_fighter
    round_count += 1
    if (round_count%5==0 and round_count < ROUND_LIMIT):
        print('+---------+')
        print(f"| Round {int(round_count/5)+1} |")
        print('+---------+')

# rounding to 0 negative stamina numbers
if (attack_fighter.stamina < 0):
    attack_fighter.stamina = 0
if (defense_fighter.stamina < 0):
    defense_fighter.stamina = 0

# displaying the results of the match
if (ko_occurred == True):
    print(f"\n{attack_fighter.name} won the match by KO!")
elif (attack_fighter.stamina > defense_fighter.stamina and defense_fighter.stamina == 0):
    print(f"\n{attack_fighter.name} won the match by Technical KO!")
elif (defense_fighter.stamina > attack_fighter.stamina and attack_fighter.stamina == 0):
    print(f"\n{defense_fighter.name} won the match by Technical KO!")
elif (attack_fighter.stamina > defense_fighter.stamina and defense_fighter.stamina > 0):
    print(f"\n{attack_fighter.name} won the match on points! ({attack_fighter.stamina}pt/{defense_fighter.stamina}pt)")
elif (defense_fighter.stamina > attack_fighter.stamina and attack_fighter.stamina > 0):
    print(f"\n{defense_fighter.name} won the match on points! ({defense_fighter.stamina}pt/{attack_fighter.stamina}pt)")
else:
    print("Incredible, it's a tie! Both fighters still stands.")