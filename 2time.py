seconds=int(input("enter seconds:"))
hours=seconds//3600
minutes=(seconds%3600)//60
secs=seconds%60
print("time:",hours, "hours",minutes, "minutes",secs,"seconds")