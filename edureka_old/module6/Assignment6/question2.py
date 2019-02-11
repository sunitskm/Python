#I used randint so that you can see the value. Else in rand it appeards differently
import numpy as np;
#arr = np.random.rand(100,1)
arr = np.random.randint(100,size=(50,1))
#print(arr)
maximum = arr.max()
minimum = arr.min()
print(maximum)
print(minimum)
arr[arr==maximum] = 0
arr[arr==minimum] = 100
print(arr)
