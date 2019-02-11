import random
import string
uc = string.ascii_uppercase
lc = string.ascii_lowercase
di = string.digits
spsym = "!@#$%Z^&*()?"
password = ''.join(random.choices(uc+lc+di+spsym,k=6))
print(password)
print(dir(random))
