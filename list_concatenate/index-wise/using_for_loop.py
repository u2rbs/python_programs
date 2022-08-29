list1 = ["M", "na", "i", "Ja"]
list2 = ["y", "me", "s", "ck"]
list3 = []
for i in list1:
    for j in list2:
        if list1.index(i) == list2.index(j):
            list3.append(i+j)
print(list3)
