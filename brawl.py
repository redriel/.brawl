import fighter
import recruiter
import random
ROUND_LIMIT = 14

print(".brawl started")

recruiter = recruiter.Recruiter('roster.json')
fighter_one = recruiter.select(input("Chose fighter 1: "))
fighter_two = recruiter.select(input("Chose fighter 2: "))

# fighter_one = fighter.Fighter(
#     "ryu", "a true master of martial arts", "dragon punch", 100, 7, 85, 20, 4, 5, 15)
# fighter_two = fighter.Fighter(
#     "ken", "an incredible opponent", "dragon kick", 100, 9, 79, 20, 5, 2, 3)

fighter_one.announce()
fighter_two.announce()


if (fighter_one.nimble > fighter_two.nimble):
    attack_fighter = fighter_one
    defense_fighter = fighter_two
else:
    attack_fighter = fighter_two
    defense_fighter = fighter_one

round_count = 0
print(f"Round {round_count+1}")

while (attack_fighter.stamina > 0 and defense_fighter.stamina > 0 and round_count <= ROUND_LIMIT):
    tecnique_chance = random.randint(0, 99)
    tecnique_scored = False
    if (attack_fighter.books >= tecnique_chance):
        attack = attack_fighter.tecnique
        print(f"{attack_fighter.name} throws a {attack_fighter.tecnique_name}!")
        tecnique_scored = True
    else:
        attack = attack_fighter.punchforce
        
    elusion_chance = random.randint(0, 99)
    if (defense_fighter.nimble >= elusion_chance):
        attack = 0
    if (elusion_chance >= 49):
        attack -= defense_fighter.tough
    if (attack < 0):
        attack = 0
    defense_fighter.stamina -= attack

    print(f"{attack_fighter.name} dealt {attack} dmg to {defense_fighter.name}.")

    if (tecnique_scored):
        ko_chance = random.randint(0, 99)
        if (defense_fighter.guts < ko_chance):
            defense_fighter.stamina = 0
            print(f"{defense_fighter.name} is knocked out!")
            break

    attack_fighter, defense_fighter = defense_fighter, attack_fighter
    round_count += 1
    if (round_count%5==0 and round_count < ROUND_LIMIT):
        print(f"Round {int(round_count/5)+1}")

if (attack_fighter.stamina < 0):
    attack_fighter.stamina = 0
if (defense_fighter.stamina < 0):
    defense_fighter.stamina = 0

if (attack_fighter.stamina > defense_fighter.stamina):
    print(f"\n{attack_fighter.name} won the match with {attack_fighter.stamina} hp left")
    print(f"{defense_fighter.name} lost the match with {defense_fighter.stamina} hp left")
else:
    print(f"\n{defense_fighter.name} won the match with {defense_fighter.stamina} hp left")
    print(f"{attack_fighter.name} lost the match with {attack_fighter.stamina} hp left")
