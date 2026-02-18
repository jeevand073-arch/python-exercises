wrd = input('ente the word')
i = len(wrd)
revers = ""

while i >= 0 :
    revers +=wrd[i]
    i-=1
print(revers)