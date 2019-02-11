x=1
y=2
total = 0
z = 0
while(y<4000000):
    if(y%2 == 0):
        total = total + y
    z = x+y
    x = y
    y = z
print(total)
