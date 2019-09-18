
def most_frequent(ar):
    dict1 = {}
    for i in ar:
        if(i in dict1):
            dict1[i]+=1
        else:
            dict1[i] = 1
    print(dict1.keys())
    lar = 0
    l = []
    for i in dict1.keys():
        freq = int(dict1[i])
        print(type(freq))
        if(lar==freq):
            lar = dict1
            l = []
            l.append(i)
        elif(freq==lar):
            l.append(i)
    print(l)
most_frequent([1,2,3,1,4,3,2,6])
