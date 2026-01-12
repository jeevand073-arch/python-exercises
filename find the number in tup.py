
tup=(90,100,20,700,200)
largest=tup[0]
smalle=tup[0]

for i in range(len(tup)):
    if tup[i] > largest:
        largest=tup[i]
    
    if tup[i] < smalle:
        smalle=tup[i]

print(largest)
print(smalle)