l = [int(i) for i in input().split()]
s = set()
def recurring(l):
    for i in range(len(l)):
        if(l[i] not in s):
            s.add(l[i])
        else:
            return(l[i])
    return None
print(recurring(l))
