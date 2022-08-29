# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# expected output 
# 10 400
# 20 300
# 30 200
# 40 100

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
list2.reverse()

for i, j in zip(list1, list2):
    print(f"{i} {j}")
