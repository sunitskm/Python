dict1 = {'a':1,'b':2}
k = dict1.keys()
v = dict1.values()
#print(k)
#print(v)
#print(zip(v,k))
rev_dict1 = {i:j for (i,j) in zip(v,k)}
print(rev_dict1)
