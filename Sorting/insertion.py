print("Enter numbers to be sorted")
l = [int(i) for i in input().split()]
#print(l)
for i in range(1,len(l)):
    num = l[i]
    j=i-1
    while(j>=0 and l[j]>num):
        l[j+1]=l[j]
        j=j-1
    l[j+1]=num
print(l)
