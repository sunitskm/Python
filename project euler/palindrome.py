def isPalindrome(n):
    n1 = n
    rev = 0
    d = 0
    while(n1!=0):
        d = n1%10
        rev = rev*10 + d
        #print(rev)
        n1 = n1//10
    if rev == n:
        return(True)
    #print (rev)
    return(False)
largest = 0
for i in range(999,99,-1):
    #print("Hello")
    for j in range(999,99,-1):
        n = i*j
        if (isPalindrome(n)):
            if n>largest:
                largest = n
print(largest)
