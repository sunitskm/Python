def bin_recur(digit, prefix = ""):
    print("bit_recur(" + str(digit) + ", " + prefix+")" )
    if(digit == 0):
        print(prefix)
        
    else:
        bin_recur(digit-1,prefix=prefix+"0")
        bin_recur(digit-1,prefix=prefix+"1")
bin_recur(4)
