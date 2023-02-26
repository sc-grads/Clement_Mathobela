with open('american-english.txt') as file:
    content = file.read().splitlines()


    my_dict = dict()
    for w in content:
        my_dict[w] = len(w)

    for k, v in my_dict.items():
        print(f'{k} : {v}')