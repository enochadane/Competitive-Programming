def insertionSort(lst):
    for i in range(1, len(lst), 1):
        j = i
        while j > 0 and lst[j] < lst[j - 1]:
            lst[j], lst[j - 1] = lst[j - 1], lst[j]
            j -= 1
        print(lst)

    return lst

insertionSort([2,0,2,1,1,0])