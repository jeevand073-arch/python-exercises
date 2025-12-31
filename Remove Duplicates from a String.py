wrd = "programming"
store = ''
for i in wrd :
    if i not in store :
        store+=i
print(store)
    # or
#  using function dict.fromkeys
s = "programming"
result = "".join(dict.fromkeys(s))
print(result)

