n=int(input("enter a number to gerenate fibo series:"))
a,b=0,1
print(a,end=' ')
print(b,end=' ')
for i in range(1,n-1):
    c=a+b
    print(c,end=' ')
    a=b
    b=c

    

