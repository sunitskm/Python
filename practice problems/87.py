file = open("countries-missing.txt","r")
content = file.readlines()
content = [i.strip("\n") for i in content]
checklist = ["Portugal","Germany","Spain"]
updated_content = content + checklist
updated_content.sort()
print(updated_content)
