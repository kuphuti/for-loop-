a=1
for i in range(1,6,+2):
    for j in range(6-i):
        print(" ",end="")
    for k in range(i):
        print("*",end=" ")
    for l in range(3,0):
        print("*",end=" ")    
    print()        