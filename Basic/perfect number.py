n=int(input("enter a number:"))
sum=0
for i in range(1,int(n/2)+1):
    if(n%i==0):
      sum=sum+i
if(n==sum):
    print("perfect number")

else:
    print("not a perfect number ")
