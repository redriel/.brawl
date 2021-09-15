import fighter
import json
class Recruiter:
    def __init__(self, roster_file):
        self.roster_file = roster_file

    def select(self, selected_fighter):
        f = open(self.roster_file)
        roster = json.load(f)
        
        i = 0
        found = False
        while(i < len(roster['roster']) and found == False):
            if(roster['roster'][i]['name'] == selected_fighter):
                found = True
            if (found == False):
                i += 1
        
        if (found == True):
            values = list(roster['roster'][i].values())
            new_fighter = fighter.Fighter(values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7], values[8], values[9])
            f.close()
            return new_fighter
        else:
            print('Fighter not found')
            return None