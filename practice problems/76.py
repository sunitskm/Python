from datetime import datetime
#Today is Wednesday, December 28, 2016
date_var = datetime.now()
print("Today is " + date_var.strftime("%A") + ", "+date_var.strftime("%B") + " " + date_var.strftime("%d") + ", "+ date_var.strftime("%Y"))
print(date_var.strftime("Today is %A, %B %d, %Y"))

yob = int(input("Enter your year of birth: "))
cy = datetime.now().year
print("Your age is "+str(cy-yob))
