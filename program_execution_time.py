import time

t1 = time.time()
for i in range(10):
    print("Python")
t2 = time.time()

print(f"execution time: {t2 - t1}")
