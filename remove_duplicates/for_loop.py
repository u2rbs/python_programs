list1 = [1, 2, 3, 3, 2, 1]
new_list = []
for i in list1:
    if i not in new_list:
        new_list.append(i)
print(new_list)
