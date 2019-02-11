calls = 0
def dice_addition(dice,total):
    dice_addition_helper(dice,total,set_dice=[])
    print(calls)

def dice_addition_helper(dice,total,set_dice=[]):
    global calls
    calls = calls+1
    if(total<0):
        return
    elif(total==0 and dice==0):
        print(set_dice)
    elif(dice==0):
        return
    else:
        for i in range(1,7):
            if(total>=i+(dice-1)*1 and total<=i+(dice-1)*6):
                set_dice.append(i)
                dice_addition_helper(dice-1,total-i,set_dice)
                del set_dice[-1]
dice_addition(3,7)
