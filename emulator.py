import fighter
import recruiter
import random
ROUND_LIMIT = 14

def battle(fighter_one, fighter_two):
    # fastest fighter starts first
    if (fighter_one.nimble > fighter_two.nimble):
        attack_fighter = fighter_one
        defense_fighter = fighter_two
    else:
        attack_fighter = fighter_two
        defense_fighter = fighter_one

    round_count = 0
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

        # if a tecnique occurs, the match could be over
        ko_occurred = False
        if (tecnique_scored and elusion_scored == False):
            ko_chance = random.randint(0, 99)
            if (defense_fighter.guts < ko_chance):
                defense_fighter.stamina = 0
                ko_occurred = True
                break
        
        # swapping attacking e defendig fighters and carrying on with the match
        attack_fighter, defense_fighter = defense_fighter, attack_fighter
        round_count += 1

    # rounding to 0 negative stamina numbers
    if (attack_fighter.stamina < 0):
        attack_fighter.stamina = 0
    if (defense_fighter.stamina < 0):
        defense_fighter.stamina = 0

    # displaying the results of the match
    if (ko_occurred == True):
        return attack_fighter
    elif (attack_fighter.stamina > defense_fighter.stamina and defense_fighter.stamina == 0):
        return attack_fighter
    elif (defense_fighter.stamina > attack_fighter.stamina and attack_fighter.stamina == 0):
        return defense_fighter
    elif (attack_fighter.stamina > defense_fighter.stamina and defense_fighter.stamina > 0):
        return attack_fighter
    elif (defense_fighter.stamina > attack_fighter.stamina and attack_fighter.stamina > 0):
        return defense_fighter
    else:
        return attack_fighter


recruiter = recruiter.Recruiter('roster.json')


megaindex = 0
stats = {}
while(megaindex < 1000):
    fighters = []
    winners = []
    i = 0
    while (i < 30):
        fighters.append(recruiter.get_fighter(i))
        i += 1

    fighters.append(fighter.Fighter('dummy1', 'dummy1', 'dummy1', 1, 1, 1, 1, 1, 1, 1))
    fighters.append(fighter.Fighter('dummy2', 'dummy2', 'dummy2', 1, 1, 1, 1, 1, 1, 1))

    random.shuffle(fighters)
    i = 0
    j = i + 1
    while (j <= len(fighters) and len(fighters) > 1):
        winner = battle(fighters[i], fighters[j])
        winners.append(winner)
        i += 2
        j = i + 1
        if(len(winners) * 2 == len(fighters)):
            fighters = winners
            winners = []
            i = 0
            j = i + 1
    
    value = stats.get(fighters[0].name)
    if (value is None):
        stats.update({fighters[0].name : 1})
    else:
        value += 1
        stats.update({fighters[0].name : value})
    megaindex += 1
    
stats = sorted(stats.items(), key=lambda x: x[1], reverse=True)
total = 0
for fighter in stats:
    total = total + (int(fighter[1]))
for fighter in stats:
  print(f"{float((fighter[1]*100) / total)}%___{fighter[0]}")