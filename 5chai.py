file=open("demo.txt","r")
count=1
for line in file:
    print(count," : ", line)
    count+=1
file.close()