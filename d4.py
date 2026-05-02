num = int(input("Enter a number: "))

for i in range(num):
    for j in range(num):
        if i == 0:
            print("#", end="")
    print()