password = str(input("Enter a password: "))
print(password)
if(len(password)>=5 and any([i.isupper() for i in password]) and (any([i.isdigit() for i in password]))):
    print("Password is fine")
else:
    print("Password is incorrect")

password = str(input("Enter a password: "))
print(password)
if(not len(password)>=5):
    print("Password is too short")
elif (not any([i.isupper() for i in password])):
    print ("Your password should have an uppercase letter in it")
elif (not any([i.isdigit() for i in password])):
    print("Your password should have a digit")
else:
    print("Password is fine")
