a = [1,2,3,4,5,6,7,8]
def recur_print(a):
    if(len(a)==1):
        print(a[0],end= " ")
    else:
        recur_print(a[:1])
        recur_print(a[1:])
recur_print(a)
