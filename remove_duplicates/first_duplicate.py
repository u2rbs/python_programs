def find_first_duplicate(list1):
    new_list = []
    for i in list1:
        if i not in new_list:
            new_list.append(i)
        elif i in new_list:
            return i

nums = [1, 2, 3, 4, 5, 6, 2, 3, 4, 1, 2]
first_dup = find_first_duplicate(nums)
print(first_dup)
