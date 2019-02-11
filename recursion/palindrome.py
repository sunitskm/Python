a = "madam"
def is_palin(s):
    if(len(s)==1):
        return s
    else:
        return is_palin(s[1:])+s[0]
print(is_palin(a)==a)
