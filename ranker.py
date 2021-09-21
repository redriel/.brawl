# Evaluator for fighters in roster.json

import json

roster_file = 'roster.json'
f = open(roster_file)
roster = json.load(f)
ranking = {}

i = 0
while(i < len(roster['roster'])):
    current_fighter = roster['roster'][i]
    rank = (current_fighter['punchforce'] * ((current_fighter['stamina']) / 100)) + \
    ((current_fighter['nimbleness'] + (current_fighter['toughness'] / 2)) * ((current_fighter['guts']) / 100)) + \
    ((current_fighter['tecnique'] * ((current_fighter['books']/100))) / 100)
   
    rank = int(round(rank))
    if (current_fighter['books'] >= 10):
        rank += 3
    if (current_fighter['nimbleness'] >= 10):
        rank += 2
    if (current_fighter['toughness'] >= 10):
        rank += 1

    ranking.update({current_fighter['name'] : rank})
    i += 1

ranking = sorted(ranking.items(), key=lambda x: x[1], reverse=True)
for fighter in ranking:
  print(f"{fighter[0]}: {fighter[1]}")