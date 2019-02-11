import numpy as np;
arr = np.random.randint(10,size=(10,2))
print(arr)
def cart2pol(x, y):
    theta = np.arctan2(y, x)
    rho = np.hypot(x, y)
    return [theta, rho]
li_pol = []
for i in arr:
    l = cart2pol(i[0],i[1])
    li_pol.append(l);
arr_pol = np.asarray(li_pol)
print(arr_pol)
