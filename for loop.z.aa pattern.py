chr=input("enter chr")
for i in range(0,len(chr)):
    for j in range(0,i+1):
        print(chr[j],end=" ")
    print()    