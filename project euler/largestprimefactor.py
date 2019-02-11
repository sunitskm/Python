import math
def isPrime(n):
    sq_n = n**0.5
    ce_se_n = math.ceil(sq_n)
    for i in range(2,ce_se_n+1):
        if (n%i==0):
            return(False)
    return(True)
def findLargest(n):
    if n<2:
        return("No prime factors")
    else:
        larPrime = 2
    num = math.ceil(n**0.5)+1
    for i in range(2,num):
        if(n%i == 0):
            if(isPrime(i)):
                if i>larPrime:
                    larPrime = i
            if(isPrime(n//i)):
                if n//i > larPrime:
                    larPrime = n//i

    print("Largest Prime is " + str(larPrime))
#print(isPrime(15359))
findLargest(600851475143)
