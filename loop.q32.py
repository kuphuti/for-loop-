a=int(input("enter a"))
sum=0
i=1
while i<=a:
    if i%2==0:
        print("+",i*i,end=" ")
    else:
        print("-",i*i,end=" ")
    i=i+1