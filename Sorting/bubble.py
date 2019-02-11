print("Enter numbers to be sorted")
l = [int(i) for i in input().split()]
#print(l)
for i in range(len(l)):
    print(l)    
    for j in range(len(l)-1):
        if(l[j]>l[j+1]):
            temp = l[j]
            l[j] = l[j+1]
            l[j+1] = temp
