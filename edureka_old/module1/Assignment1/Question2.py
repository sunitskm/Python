s = "www.edureka.in"
s1 = ".edureka"
ind = s.index(s1)
ind_after = s.index(s1)+ len(s1)
s2 = s[0:ind].replace('w','') + s[ind:ind+len(s1)] + s[ind+len(s1):].replace('w','')
print(s2)
s3 = s.replace(s,'')
print("Hello %s" %(s3))
list_s4 = []
for i in s:
    temp = s.index(i)
    if((temp<ind or temp>ind_after) and i.islower):
        pass
    else:
        list_s4.append(i)
s4 = ''.join(list_s4)
print(s4)

type1 = type(0X7AE)
print(type1)
type2 = type(3+4j)
print(type2)
print(type((-01234)))
print(type((3.14e-2)))
#print('%c' %('a'))
