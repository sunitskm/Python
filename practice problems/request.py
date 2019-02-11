import requests
import webbrowser
import pandas
from matplotlib import pyplot as plt
#from urllib.requests import urlopen
'''r = requests.get("http://www.pythonhow.com/universe.txt")
print(r.text[:100])
print(__name__)'''
data = requests.get("http://www.pythonhow.com/data/universe.txt")
text = data.text
#print(text)
numofa = len([i for i in text if i.lower() == 'a'])
print(numofa)




#query=input("Enter your Google query: ")
#webbrowser.open_new_tab("https://www.google.com/search?q="+query)

data = requests.get("http://www.pythonhow.com/data/sampledata.txt")
text = data.text
print(text)
listofsentences = text.split("\n")
print(listofsentences)
with open("sampledata_x_2.txt",'w') as file:
    file.write(listofsentences[0])
    for i in range(1,len(listofsentences)):

        list_num_per_line = listofsentences[i].split(',')
        first_2 = int(list_num_per_line[0])*2
        second_2 = int(list_num_per_line[1])*2
        total_string = str(first_2)+","+str(second_2)
        file.write("\n"+total_string)


data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
print (data)
data = data*2
data.to_csv("sampledata_x_csv.txt",index = None)

data1 = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data2 = pandas.read_csv("http://pythonhow.com/data/sampledata_x_2.txt")
data12 = pandas.concat([data1,data2])
print(data12)
#data12.to_csv("sampledata12.txt", index=None)
data12.plot(x = 'x',y = 'y',kind = 'scatter')
plt.show()
