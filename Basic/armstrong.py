n=int(input("Enter a number:"))
temp=n
x=len(str(n))
sum=0
while(n>0):
    r=n%10
    sum=sum+r**x
    n=n//10
if temp==sum:
    print("The given number is an armstrong")
else:
    print("The given number is not an armstrong")
    
