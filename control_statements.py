# 28-01-2021

first_int = 10
second_int = 20
if first_int > second_int:
    print('The first int is bigger!')
else:
    print('The second int is bigger!')

num = [1, 2, 3, 4]
for value in num:
    print(value)

for index, value in enumerate(num):
    print(index, value)

print("\nEnumerate")
for index, value in enumerate(num[2:4], 2):
    print(index, value)

for value in enumerate(num):
    print(value)

for i in range(1, 10):
    print(i)


