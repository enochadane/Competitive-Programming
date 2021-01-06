def countingSort(lst):
    max = 0
    sortedArray = []
    for i in range(len(lst)):
        if(lst[i] > max):
            max = lst[i]
    countArray = [0] * (max + 1)
    for i in range(len(lst)):
        countArray[lst[i]] += 1
    for i in range(len(countArray)):
        for j in range (countArray[i]):
            sortedArray.append(i)
    print(sortedArray)
    return sortedArray

countingSort([1, 2, 3, 1, 3])