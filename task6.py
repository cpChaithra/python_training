num=int(input("enter a number"))
for i in range(num):
    for j in range(num):
       if i==0 or j==0 or j==num :
        print("#", end=" ")
       else:
        print(" ",end=" ")
    print()
