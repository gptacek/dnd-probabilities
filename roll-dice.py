import random
from itertools import product

#roll _d_, e.g. 1d20 to roll a single 20 sided dice.  or 3d6 for three 6 sided dice
def roll_dice(num_die, die_val):
    min = 1
    max = die_val

    print("Rolling", num_die, die_val, "sided dice")
    for x in range(1, (num_die+1)):
        print("Roll ", x)
        print(random.randint(min, max))

#helper function to get coefficient for probability of getting exact values from dice rolls
def poss_combinations(dice, faces, number):
    choices = product(range(1, faces+1), repeat=dice)
    return sum(sum(roll) == number for roll in choices)

#likelihood for a roll for dice of one type to meet a given value or above
def prob_meet(num_die, die_val, meet_val):
    max_val = num_die * die_val
    total_poss = die_val ** num_die
    if max_val < meet_val:
        return 0
    else:
        #print("die_val", die_val)
        #print("num_die", num_die)
        #print("tot",total_possibilites)
        combination_vals = []
        for x in range(meet_val, max_val+1):
            app_val = poss_combinations(num_die, die_val, x)
            combination_vals.append(app_val)
        return round(sum(combination_vals)/total_poss, 3)
#print(prob_meet(3,6,10))

# gives probability of reaching or surpassing the meet_value
# current rule: maximum 1d20 and 1 other type of die (but can have multiple dice)
# string is the other die (d4, d6, d8, d10, d12)
# e.g. 1d4 or 2d4 or 1d6...
def affect_d20(string, meet_val):
    num_die = int(string[0])
    die_val = int(string[2:])
    
    start_prob = (20-(meet_val-1))/20
    
    max_change = num_die*die_val
    combination_vals = []
    for x in range(num_die, max_change+1):
        app_val = poss_combinations(num_die, die_val, x)
        combination_vals.append(app_val)
    prob_vals = []
    for x in range(len(combination_vals)):
        prob_vals.append(sum(combination_vals[x:])/(sum(combination_vals)))
    add_prob = sum(prob_vals)*.05
    for x in range(1, num_die):
        add_prob += .05
    return(start_prob + add_prob)


print(affect_d20("1d4", 15))

# gives probability of reaching or surpassing the meet_value but takes 
# a modifier to an attack into account (e.g. proficiency bonus and dex/str mod
# for weapons or wis/int/cha for spell attacks)
def attack_to_hit(string,meet_val,attack_mod):
    return affect_d20(string,(meet_val-attack_mod))

print(attack_to_hit("1d4", 17, 2))