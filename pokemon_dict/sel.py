print('1 2 3 4 5 6 7 8 9 10')

for x in range(1, 11):
    print(x, end=' ')
    for y in range(1, 11):
        print(x * y, end=' ')
    print()
