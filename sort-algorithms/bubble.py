def bubbleSort(list lst1):
    for(i in range len(lst1) - 1):
        for( j in range len(lst1) - i):
            int temp = lst1[i]
            lst1[i] = lst1[j]
            lst1[j] = temp


    return lst1

bubbleSort([4, 3, 2, 1])