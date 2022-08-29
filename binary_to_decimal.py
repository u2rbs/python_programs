num = str(1001)
count = 0
sum = 0
for i in num[::-1]:
    i = int(i)
    if count % 2 == 0:
        sum += 2**count * i
    elif count % 2 != 0:
        sum += 2**count * i
    count += 1

print(sum)
