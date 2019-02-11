def subset(names,choices=[]):
    if(len(names)==0):
        print(choices)
    else:
        choices.append(names[0])
        subset(names[1:],choices)
        del choices[-1]
        subset(names[1:],choices)
subset(["Sunit","Mishra"])
