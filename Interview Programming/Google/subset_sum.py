l = [int(i) for i in input().split()]
num = int(input())
#print(num)
#print(l)
def subset(l):
    tot = 0
    ch = []
    subsetHelper(l,tot,num,ch)
def subsetHelper(l,tot,num,ch):
    #print("("+str(l)+" "+str(tot)+" "+str(num)+" "+str(ch)+")")
    if(tot==num):
        print(ch)
    elif(tot>num or len(l)==0):
        #return "Hello"
        return
    else:
        ch.append(l[0])
        subsetHelper(l[1:],tot+l[0],num,ch)
        del ch[-1]
        subsetHelper(l[1:],tot,num,ch)
subset(l)
