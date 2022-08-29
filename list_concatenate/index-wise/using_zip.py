list1 = ["M", "na", "i", "Ja"]
list2 = ["y", "me", "s", "ck"]
list3 = []
for i, j in zip(list1, list2):
    list3.append(i+j)
print(list3)
