file = open("countries-raw.txt","r")
file_contents = file.readlines()
#print(file_contents)
content = [i.strip('\n') for i in file_contents]
#print(content)
content =  [i for i in content if len(i) > 1]
#print(content)
content = [i for i in content if i.upper() != 'TOP OF PAGE']
#print(content)
with open("countries_only.txt","w") as file:
    for i in content:
        file.write(i)
        file.write("\n")
file = open("countries_only.txt","r")
file_list = file.readlines()
print(file_list)
file_list = [i.strip("\n") for i in file_list]
checklist = ["Portugal", "Germany", "Munster", "Spain"]
refined_checklist = [i for i in checklist if i in file_list]
print(refined_checklist)
