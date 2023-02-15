# YOUR CODE STARTS HERE
file = open('a.txt')
file.seek(4)
word = file.read(5)
file.close()