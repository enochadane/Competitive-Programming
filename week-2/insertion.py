def insertionSort(lst):
    for i in range(len(lst) - 1):
        j = i + 1
        while j < len(lst) and lst[j] < lst[i]:
            lst[i], lst[j] = lst[j], lst[i]
            j += 1
    print(lst)

    return lst

insertionSort([2,0,2,1,1,0])