l = []
for i in range(5):
    k = input()
    v = int(input())
    d = {k:v}
    l.append(d)
    i = len(l)-2
    while(i>=0 and list(l[i].values())[0]>v):
        l[i+1]=l[i]
        i-=1
    l[i+1]=d
print(l)
