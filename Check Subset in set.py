A = {1, 2}
B = {1, 2, 3, 4}
c=set()
for i in B:
    if i not in A:
        c.add(i)
        print(c)