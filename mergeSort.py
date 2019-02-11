def mergeSort(list1):
    #print("Hello")
    if len(list1)>1:
        mid = len(list1)//2
        #print(mid)
        lefthalf = list1[0:mid]
        #print(lefthalf)
        righthalf = list1[mid:len(list1)]
        #print(righthalf)
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i = 0
        j = 0
        k = 0
        while(i<len(lefthalf) and j<len(righthalf)):
            print("Inside merge " + str(i))
            if(lefthalf[i]<righthalf[j]):
                list1[k] = lefthalf[i]
                i+=1
                k+=1
            if(lefthalf[i]>=righthalf[j]):
                list1[k] = righthalf[j]
                j+=1
                k+=1
        while(i<len(lefthalf)):
            list1[k]= lefthalf[i]
            i+=1
            k+=1
        while(j<len(righthalf)):
            list1[k]= righthalf[j]
            j+=1
            k+=1
list1 = [54,26,93,17,77,31,44,55,20]
mergeSort(list1)
print(list1)
