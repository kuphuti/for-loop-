n=int(input("enter"))
for i in range(n):
    for j in range(n):
        if j==n-1 or j==0 or i==0 or i==2:
            print("*",end=" ")
        else:
            print(" ",end=" ") 
    print()           