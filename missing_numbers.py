def find_missing_numbers(nums):
    new_list = []
    for i in range(1, nums[-1]):
        if i not in nums:
            new_list.append(i)
    return new_list

listOfNumbers = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16]

print(find_missing_numbers(listOfNumbers))
