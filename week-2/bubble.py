def bubbleSort(lst1):
    for i in range(1, len(lst1), 1):
        for j in range(len(lst1) - i):
            if lst1[j] > lst1[j+1]:
                lst1[j], lst1[j+1] = lst1[j+1], lst1[j]
    print(lst1)

    return lst1

bubbleSort([2,0,2,1,1,0])