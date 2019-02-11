import pandas as pd
df1 = pd.read_csv("urls.txt",header=None)
print(df1.iterrows())
with open('url_corrected.txt','w') as file:
    for index,row in df1.iterrows():
    #print(row[0])
        url_name = row[0]
        url_name_changed = url_name[:4]+url_name[5:7]+'/'+url_name[7:]
        #print(url_name_changed)
        file.write(url_name_changed+"\n")

with open('url_corrected_1.txt','w') as file:
    for index,row in df1.iterrows():
    #print(row[0])
        url_name = row[0]
        url_name = url_name.replace('/','//')
        url_name = url_name.replace('s','',1)
        print(url_name)
        file.write(url_name+"\n")
