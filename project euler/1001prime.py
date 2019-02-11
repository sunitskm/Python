import math
def isPrime(n):
    sq_n = n**0.5
    ce_se_n = math.ceil(sq_n)
    for i in range(2,ce_se_n+1):
        if(n==2):
            return(True)
        if (n%i==0):
            return(False)
    return(True)
n=2
i = 0
list_prime = []
while(i!=10001):
    if(isPrime(n)):
        i+=1
        list_prime.append(n)
        if (i==10001):
            print(n)
    n+=1
#print(n-1)
print(isPrime(104759))
#print(list_prime)
