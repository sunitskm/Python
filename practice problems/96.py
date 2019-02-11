item = ""
file = open('feed_input.txt','a+')
while item.upper() != "CLOSE":
    item = input("Enter a value: ")
    if(item.upper()!='SAVE' and item.upper()!='CLOSE'):
        file.write(item+'\n')
    if(item.upper()=='SAVE'):
        file.close()
        file = open('feed_input.txt','a+')
file.close()
