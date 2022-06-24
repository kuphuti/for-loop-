for i in range(1,6):
    for j in range(1,6):
        if j==5 or i==j or j==1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j=j+1
    print()            