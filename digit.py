n=int(input("enter a digit number"))
count = 1         
while n != 0:
    n = n // 10
    count += 1

print("Digits =", count)