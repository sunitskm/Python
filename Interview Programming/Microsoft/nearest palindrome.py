def isPalindrome(n):
    n1 = n
    n2 = n+1
    while(True):
        n1_str = str(n1)
        n2_str = str(n2)
        if(n1_str==n1_str[::-1]):
            print(n1)
            break
        if(n2_str==n2_str[::-1]):
            print(n2)
            break
        n1-=1
        n2+=1
print("Enter a number")
n = int(input())
isPalindrome(n)
