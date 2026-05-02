num=int(input("enter a number:"))
original=num
total=0
while num>0:
    last=num%10
    total=total+last**3
    num=num//10
if original==total:
    print("armstrong")
else:
    print("not armstrong")