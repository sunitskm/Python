#Could not find any other way to do. Feel free to share any idea regarding this problem.
import scipy as sp;
v = sp.zeros((10,10))
l= []
print(v.shape)
for i in range(v.shape[0]):
    for j in range(v.shape[1]):
        if(i==j):
            v[i][j] = 2
        if(abs(i-j)==2):
            v[i][j] = 1;

print(v)
