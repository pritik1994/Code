import math

def jumSearch(arr,n,x):
    step = math.sqrt(n)
    fun =  math.sqrt(n)
    prev = 0
    while arr[int(min(step,n)-1)]<x:
              prev = step
              step = step + fun
              if prev > n:
                  prev = -1
                  break
                  
    print(prev)
    if prev == -1:
       print"element not found"
    else:
       while (arr[int(prev)])<x:
          prev += 1
       if arr[int(prev)] == x:
          print"element found"
          
n = input("enter number of inputs")
k = input("enter search elements")
arr = [n]
for i in range(0,n):
    i = input()
    arr.append(i)
jumSearch(arr,n,k)


        
    
