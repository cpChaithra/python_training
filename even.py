num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print("Welcome")
elif num % 3 == 0:
    print("Hello")
elif num % 3 == 0 or num % 5 == 0:
    print("Quick")
else:
    print(" not divisible by 3 or 5")