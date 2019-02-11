a = 4
b = 4
def power(a,b):
    if(b==1):
        return a
    else:
        return power(a,b-1)*a
print(power(a,b))
