l = [int(i) for i in input().split()]
def add_one(l):
    carry = 1
    l_final = []
    for i in range(1,len(l)+1):
        #print(l[-i])
        tot = l[-i]+carry
        if(tot==10):
            l_final.insert(0,tot%10)
        else:
            carry = 0
            l_final.insert(0,tot%10)
    if(carry==1):
        l_final.insert(0,1)
    return l_final
print(add_one(l))
