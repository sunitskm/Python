num = 2**1000
d = 0
s = 0
while(num != 0):
    d = num%10
    s += d
    num = num//10
print(s)
