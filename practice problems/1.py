from collections import OrderedDict
from pprint import pprint
import string
import math
import glob
import time
a = [i for i in range(1,21)]
print(a)

b = range(1,21);
print(list(b))

my_range = range(1, 21)
print([i*10 for i in my_range])

print([str(i) for i in my_range])

#
print(list(map(str,my_range)))


#REMOVING DUPLICATES
#1
a = ["1", 1, "1", 2]
print(list(set(a)))

#2
b = []
for i in a:
    if(i not in b):
        b.append(i);
print(b)

#3
print(list((OrderedDict.fromkeys(a))))


dict1 = {'a':1,'b':2}
print(dict1)
dict1 = dict(a=1,b=2)
print(dict1)


d = {"a": 1, "b": 2}
print(d["b"])

d = {"a": 1, "b": 2, "c": 3}
print(d["a"]+d["b"])
print(list(d.keys()))
sum_values = sum([d[i] for i in list(d.keys())])
print(sum_values)

d["d"] = 4
print(d)
print(sum((d.values())))

#Filtering items in dictionary
new_dict = {i:v for i,v in d.items() if v<=1}
print(new_dict)
new_dict = dict((key,value) for key,value in d.items() if value<=1)
print(new_dict)

dict1 = dict(a=list(range(1,11)),b=list(range(21,31)),c=list(range(31,41)))
pprint(dict1)

print(dict1['b'][2])
for k,v in dict1.items():
    print(k + " has the value " + str(v))

for letter in string.ascii_lowercase:
    print(letter, end = " ")

#printing number from 1 to 10
print()
for i in range(1,11):
    print(i)

def acceleration(v1,v2,t1,t2):
    a = (v1-v2)/(t1-t2)
    return a
print(acceleration(0,10,0,20))


def volume(h,r=10):
    vol = (4*math.pi*r*r*r/3)-(math.pi*h*h*(3*r-h)/3)
    return vol
print(volume(2))

def func(string):
    l = string.split()
    print(len(l))
func("Hello my name is The white wolf")


def countWordsFromFile(file):
    f = open(file,'r')
    print(file,end = " ")
    print(f,)
    f_contents = f.read()
    var1 = f_contents.split()
    print(len(var1))
countWordsFromFile("words1.txt")


def countWordsFromFileComma(file):
    f = open(file,'r')
    f = f.read()
    f = f.replace(',', ' ')
    l = f.split()
    print(len(l))
countWordsFromFileComma("words2.txt")

print(int(math.sqrt(9)))

def writeLetterToFile(f):
    f_read = open(f,"w");
    for l in string.ascii_lowercase:
        f_read.write(l+"\n")
writeLetterToFile("text3.txt")

#using zip
a = list(range(1,4))
b = list(range(4,7))
for i in zip(a,b):
    print(i[0]+i[1])


#2 letters in one line of a file

with open("letters2ineachline.txt","w") as file:
    count = 0
    for l in string.ascii_lowercase:
        if (count==2):
            count = 1
            file.write("\n"+l)
        else:
            count+=1
            file.write(l)
#3 letters in one letters2ineachline
with open("letters3ineachline.txt","w") as file:
    count = 0
    for l in string.ascii_lowercase:
        if(count == 3):
            count = 1
            file.write("\n"+l)
        else:
            count+=1
            file.write(l)
for l in string.ascii_lowercase:
    file_name = l+'.txt'
    with open(file_name,"w") as file:
        file.write(l)

#print(glob.glob("letters/*.txt"))
list_of_letters = glob.glob("letters/*.txt")
final_list = []
for l in list_of_letters:
    with open(l,"r") as file:
        final_list.append(file.read())

print(final_list)

#using glob
list_of_letters = glob.glob("letters/*.txt")
final_list = []
for l in list_of_letters:
    with open(l,"r") as file:
        letter = file.read()
        if(letter.lower() in 'python'):
            final_list.append(letter)

print(final_list)


#60 infinite printer
'''while True:
    print("Hello")
'''
'''while True:
    print("Hello")
    time.sleep(2)
'''

'''i = 1
while True:
    time.sleep(i)
    print("Hello")
    i+=1
'''
'''i=0
while True:
    time.sleep(i)
    print("Hello")
    if(i==3):
        print("End of loop")
        break
    i+=1
'''
d = dict(weather = "clima",earth = "terra",rain="chuva")
word = input("Enter word: ")
word = word.lower()
if(word in list(d.keys())):
    print(d[word])
else:
    print("Word not found in dictionary")
