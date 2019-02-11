def dice(num,prefix=""):
    if(num==0):
        print(prefix, end = " ")
    else:
        for i in range(6):
            dice(num-1,prefix=prefix+str(i+1))
dice(3,prefix="")
