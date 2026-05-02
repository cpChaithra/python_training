# list is a collection of heterogeneous objects  where is defined inside[] is mutable allows duplicates and ordered 

lst=[1,2,3,4,5]
print(type(lst))
print(lst[0])
lst.append(4)
print(lst)

lst.insert(2,6)
lst.extend([7,8,9])
print(lst.count(4))
print(lst.index(5))

lst.remove(9)
print(lst)
lst.pop()
print(lst)
lst.pop(3)
print(lst)
lst.remove(4)
print(lst)
lst.clear()
print(lst)
lst=[45,78,25,36,67,89]
print(lst)
lst.sort()
print(lst)
