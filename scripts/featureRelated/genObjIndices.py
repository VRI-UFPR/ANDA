with open('dataset.txt', 'w') as fd:
    for i in range(0,10000):
        print(i, file=fd)
