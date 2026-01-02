lst = [10,45,2,89,33]
largest = lst[0]
smallest =lst[0]

for i in lst :
    if i > largest:
        largest=i
    if i < smallest:
        smallest=i
print("the largest number is",largest)
print("smalest number is here",smallest)