# Write a Python script that finds the first 100 longest words in a file.

with open('american-english.txt') as file:
    words = file.read().splitlines()
    words_and_length = dict()
    for w in words:
        words_and_length[w] = len(w)
    words_list = sorted(words_and_length.items(), key=lambda x:x[1], reverse=True)
    print(words_list[:100])