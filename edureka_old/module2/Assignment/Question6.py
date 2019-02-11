from string import ascii_uppercase
D1 = {}
#print(enumerate(ascii_uppercase))
#for i,j in enumerate(ascii_uppercase):
D1 = {i:j+1 for j,i in enumerate(ascii_uppercase)}
print(D1) 
  
