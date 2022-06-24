for i in range(6):
    for j in range(1,5):
        if i==0 or j==1 or j==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()            