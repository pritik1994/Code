def binarySearch(arr,low,up,search):
    flag = False
    if up >= low:
        mid = (up+low)/2
        if arr[mid] == search:
            print("elemet found")
            return mid
        elif arr[mid] > search:
           return binarySearch(arr,low,mid,search)
        else:
           return binarySearch(arr,mid+1,up,search)
    else:
           print("not found")
           return -1



n = input("enter number of inputs")
k = input("enter search elements")
flag = False
arr = [n]
for i in range(0,n):
    i = input()
    arr.append(i)
pos = binarySearch(arr,0,n-1,k)
