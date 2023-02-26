def my_count(my_file):
    with open(my_file, 'r') as f:
        content = f.read().splitlines()
        lines = len(content)
        words = 0
        for line in content:
            words += len(line.split())

        chars = 0
        for line in content:
            chars += len(list(line))

        return lines, words, chars


print(my_count('sample_file.txt'))
