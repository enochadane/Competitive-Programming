def reverse(x):
    x = str(x)
    y = list(x)
    z = []
    reversedInt = ''
    lowerEnd = -1
    firstNonZeroIndex = 0
    if(y[0] == '-'):
        reversedInt = '-'
        lowerEnd = 0
    for i in range(len(y) - 1, lowerEnd, -1):
        z.append(y[i])
    for i in range(len(z)):
        if z[i] != '0':
            firstNonZeroIndex = i
            break
    reversedInt = reversedInt + ''.join(z[firstNonZeroIndex:])
    print(reversedInt)
    if(int(reversedInt) < -2**31 or int(reversedInt) > (2**31) - 1):
        return 0
    return reversedInt

reverse(21474836495488888)