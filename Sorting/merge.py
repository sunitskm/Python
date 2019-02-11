print("Enter numbers to be sorted")
arr = [int(i) for i in input().split()]
def merge(arr, l, m, r):
    n1 = m-l+1
    n2 = r-m
    L = [0]*n1
    R = [0]*n2
    for i in range(n1):
        L[i] = arr[l+i]
    for i in range(n2):
        R[i] = arr[m+i+1]
    i = 0
    j = 0
    k = l
    while i<n1 and j<n2:
        if(L[i]<=R[j]):
            arr[k] = L[i]
            i=i+1
        if(L[i]>R[j]):
            arr[k] = R[j]
            j=j+1
        k=k+1
    while i<n1:
        arr[k] = L[i]
        i+=1
        k+=1
    while j<n1:
        arr[k] = L[j]
        j+=1
        k+=1
def mergesort(arr,l,r):
    if l<r:
        m = (r-l)//2
        mergesort(arr,l,m)
        mergesort(arr,m+1,r)
        merge(arr,l,m,r)
n = len(arr)-1
mergesort(arr,0,n)
