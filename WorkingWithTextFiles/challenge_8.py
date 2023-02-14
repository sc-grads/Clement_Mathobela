with open('a.txt') as f:
    file1 = f.read().splitlines()

with open('b.txt') as f:
    file2 = f.read().splitlines()

new_file = list(zip(file1, file2))

i = 0
for item in new_file:
    i += 1
    if item[0] != item[1]:
        print(f'file1 ({i}): {item[0]}, file2 ({i}): {item[1]}')