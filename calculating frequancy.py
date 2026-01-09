lst = ["apple", "banana", "apple", "orange", "banana", "apple"]
fre={}

for i in lst:
    if i in fre:
        fre[i]+=1
    else:
        fre[i]=1
for x,y in fre.items():
    print(f"{x}{y} times")