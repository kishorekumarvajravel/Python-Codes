def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)
        
a=int(input("enter a no :"))
sum=0
while(a>0):
    s=a%10
    sum=sum+fact(s)
    a=a//10
print("The strong value is :",sum)