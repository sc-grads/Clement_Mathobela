# Write a Python script that finds all numbers that are divisible by 7 but are not a multiple of 5, between 1500 and 3200 (both included).

# The numbers obtained should be printed in a comma-separated sequence (CSV) on a single line.
numbers_list = list()
for i in range(1500, 3201):
    if i % 7 == 0 and i // 5 != 0:
        numbers_list.append(str(i))
numbers_str = ','.join(numbers_list)
print(numbers_str)
