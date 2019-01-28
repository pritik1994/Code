n = input("enter inputs")
arr = []
for i in range(0,n):
    i = input()
    arr.append(i)
for i in range(len(arr)):
    for j in range(0,n-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
for i in range(len(arr)):
    print(arr[i])

            
