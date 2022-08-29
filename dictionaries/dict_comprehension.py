
num = [1, 2, 3, 4, 5, 6]

# output_dictionary = {key : value for key,value in iterable [if key,value condition1]}

dict = { x: x**2 for x in num if x % 2 ==0 }

print(dict)
