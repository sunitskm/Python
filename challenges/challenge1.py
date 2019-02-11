import string
print(ord('a'))
print(ord('z'))
print(chr(65))
text = "map"
print(text)
letter = []
for l in text:
    if l.isalpha():
        int_value = ord(l)+2
        if(int_value>122):
            int_value = 96+(int_value-122)
            int_char = chr(int_value)
            letter.append(int_char)
        else:
            int_char = chr(int_value)
            letter.append(int_char)
    else:
        letter.append(l)
decrypted_string = "".join(letter)
print(decrypted_string)

intab = "KOE"
outtab = "MQG"
transtab = string.maketrans(intab,outtab)
print(text.translate(transtab))
