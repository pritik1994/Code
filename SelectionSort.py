n = input("enter number of elements")
arr = []
for i in range(0,n):
    i = input()
    arr.append(i)
for i in range(len(arr)):
    pos = i
    for j in range(i+1,len(arr)):
         if arr[pos] > arr[j]:
              pos = j
    arr[i],arr[pos] = arr[pos],arr[i]
for i in range(len(arr)):
    print(arr[i])


    
              
