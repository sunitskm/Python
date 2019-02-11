def dice_roll(dice):
    dice_roll_helper(dice,chosen = [])

def dice_roll_helper(dice,chosen):
    print("dice_roll_helper( "+str(dice)+", "+str(chosen))
    if(dice==0):
        print(chosen)
    else:
        for i in range(1,7):
            chosen.append(i)
            dice_roll_helper(dice-1,chosen)
            del chosen[-1]

dice_roll(2)
