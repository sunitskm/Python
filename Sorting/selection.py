#cerner_2^5_2019
print("Enter numbers to be sorted")
l = [int(i) for i in input().split()]
#print(l)
for i in range(len(l)):
    print(l)
    ind = i
    for j in range(i+1,len(l)):
        if(l[ind]>l[j]):
            ind = j
    temp = l[i]
    l[i] = l[ind]
    l[ind] = temp
