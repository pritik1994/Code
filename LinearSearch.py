n = input("enter number of inputs")
k = input("enter search elements")
flag = False
arr = [n]
for i in range(0,n):
    i = input()
    arr.append(i)
    
for i in arr:
   if i == k:
       flag = True
       break

if flag :
    print "element found"
else :
     print "element not found"

      
