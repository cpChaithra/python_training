u = int(input("Enter units: "))

if u <= 200:
    bill = 0
elif u <= 300:
    bill = (u - 200) * 1.5
elif u <= 400:
    bill = (100 * 1.5) + (u - 300) * 3
else:
    bill = (100 * 1.5) + (100 * 3) + (u - 400) * 7

print("Bill amount:", bill)

