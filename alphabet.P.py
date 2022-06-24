for i in range(6):
    for j in range(0,5):
        if j==0 or j==4 and i==1 or i==0 or i==2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j=j+1
    print()            