def merging(arr,low,mid,up):
    n1 = mid - low + 1
    n2 = up - mid
    arr1 = []
    arr2 = []
    arrMerge = []
    for i in range(low,n1):
        arr1.append(arr[low+i])
    for i in range(mid,n2):
        arr2.append(arr[mid+i+1])
    i = 0
    j = 0
    k = low
    while(i<n1 and j<n2):
        if(arr1[i] <= arr2[j]):
            arr[k] = arr1[i]
            i+=1
        else:
             arr[k] = arr2[j]
             j+=1
        k+=1
    while(i<n1):
        arr[k] = arr1[i]
        i+=1
        k+=1
    while(j<n2):
        arr[k] = arr2[j]
        j+=1
        k+=1

def mergeSort(arr,low,up):
    if up > low :
        mid = (low+up)/2
        return mergeSort(arr,low,mid)
        return mergeSort(arr,mid+1,up)
        return merging(arr,low,mid,up)

n = input("number of inputs")
arr = []
for i in range(0,n):
    i = input()
    arr.append(i)
mergeSort(arr,0,n)
for i in range(0,n):
    print(arr[i])

