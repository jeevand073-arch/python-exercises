A = {1, 2, 3}
B = {2, 3, 4}
c=set()

for i in A:
    if i not in B:
        c.add(i)
print(c)