n = input("number of inputs")
arr = []
for i in range(0,n):
    i  = input()
    arr.append(i)
for i in range(1,n):
    pos = i
    value = arr[i]
    while(value < arr[pos-1] and pos>0):
        arr[pos] = arr[pos-1]
        pos = pos-1
    arr[pos] = value
for i in range(0,n):
    print(arr[i])
    

        
            
