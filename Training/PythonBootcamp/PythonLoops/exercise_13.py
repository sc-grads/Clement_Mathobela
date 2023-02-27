my_sum = 0
for i in range(1, 101):
    if i % 2 == 0:
        continue
    my_sum += i
print(my_sum)

# Using while:
# my_sum = 0
# for i in range(1, 101):
#    while i % 2 != 0:
#        my_sum += i
#        break
# print(my_sum)
