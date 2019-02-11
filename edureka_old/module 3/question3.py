from operator import itemgetter
#Using itemgetter
mylist = [["john",1,"a"],["larry",0,"b"]]
m_item = sorted(mylist,key=itemgetter(1))
print(m_item)
#Using lambda function
m_lamb = sorted(mylist, key = lambda x:x[1])
print(m_lamb)
