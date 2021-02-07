# main method for running

import roll_dice

def main():
    print("Hello! Welcome to my dice probability calculator")
    print("What's the AC of your target? (no greater than 40)")
    ac = input()
    if ac.isdecimal():
        ac = int(ac)
        if ac > 40:
            print("That's too large a number!")
    else:
        print("Sorry, that's not a number")
    
    print("What is your attack modifier? (cannot exceed the ac-1)")
    atk_mod = input()
    if atk_mod.isdecimal():
        atk_mod = int(atk_mod)
        if atk_mod > ac - 1:
            print("That's too large a number!")
    else:
        print("Sorry, that's not a number")
    
    print("What die are you rolling besides the d20? (e.g. 1d6, 2d4, none)")
    dice = input()
    if dice == 'none':
        prob = roll_dice.prob_meet(1, 20, ac-atk_mod)
        return prob

    prob = roll_dice.attack_to_hit(dice, ac, atk_mod)
    
    return prob
    
print("You have a", 100*main(), "percent chance of hitting!")

#if __name__ == '__main__':
#    main()

