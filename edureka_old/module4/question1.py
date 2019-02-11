import re
input = "Hello all today is 2018-02-04 and this course continues till 2018-02-18 same as 18-2-18 and ths ssn numbers are 111-11-111 and 432-43-434 and not 11-111-11 from address 255.255.255.1 and 121.121.1.1 "
input2 = "The email addresses are 123fdhj@fdj.com , al-habibi@gmail.com , etc@etc.etc "
try:
    print("Date matches"),
    print(re.findall(r'(\b\d{4}-\d{2}-\d{2}\b)',input))
except:
    print("No matches found!")

ssn = re.compile(r'\b\d{3}-\d{2}-\d{3}\b')
print("SSN matches"),
print(ssn.findall(input))
#print(re.findall())

ipv4 = re.compile(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b")
print("ipv4 matches"),
print(ipv4.findall(input))

email = re.compile(r"\b[a-zA-z0-9_]+@[a-zA-z0-9_]+.[a-zA-z0-9_]+\b")
print("Email addresses"),
print(email.findall(input2))
