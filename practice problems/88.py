file = open("countries-by-area.txt","r")
contents = file.readlines()
contents = [i.strip("\n") for i in contents]
contents = [i for i in contents if i != '']
contents = contents[1:]
contents = [i.strip('\t') for i in contents]
final_list = []
for i in contents:
    l = i.split(',')
    l = [i.strip('\t') for i in l]
    #print(l)
    density = int(l[3])/int(l[2])
    #print(density)
    final_list.append([l[1],density])
sorted_tuple = sorted(final_list,key = lambda x:x[1],reverse = True)
for i in range(5):
    print(sorted_tuple[i][0])
