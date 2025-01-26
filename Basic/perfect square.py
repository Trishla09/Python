n=int(input("enter a number:"))
flag=0
for i in range(1,n+1):
    if i*i==n:
        flag=1
        break
if flag==1:
    print("perfect square")
else:
     print(" not a perfect square")


     



      
