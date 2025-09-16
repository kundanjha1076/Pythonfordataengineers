for i in range(1,6):
    for j in range(i,6-(i-1)):
        if (i>j):
            print(' ')
        else:
            print('*',end=' ')
    print()