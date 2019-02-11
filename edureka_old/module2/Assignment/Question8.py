l = ['a','b','c','d']
e = enumerate(l)
dict1 = {j:i+1 for i,j in e}
print(dict1)
