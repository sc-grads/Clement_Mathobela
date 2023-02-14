def my_prime(n):
    prime = True
    i = 1
    while i < n // 2:
        i = i + 1
        if n % i == 0:
            prime = False
            break
    return prime # returns True or False


my_list = list()
for n in range(1000000, 100000000):
   if my_prime(n):
       my_list.append(n)
       if len(my_list) == 5:
           break

print(my_list)