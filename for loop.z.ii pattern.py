for i in range(5):
    for j in range(5-i):
        print(" ",end=" ")
    for k in range(i+1):
        print(k+1,end=" ") 
        k=k-1    
    print()    