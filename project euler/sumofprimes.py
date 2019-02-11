import math
from datetime import datetime

def isPrime(n):
    sq_n = n**0.5
    ce_se_n = math.ceil(sq_n)
    for i in range(2,ce_se_n+1):
        if(n==2):
            return(True)
        if (n%i==0):
            return(False)
    return(True)
#for i in range(2,2000000):
start = datetime.now()
print(sum([n for n in range(2,2000000) if isPrime(n)]))
final = datetime.now()-start
print(final)
