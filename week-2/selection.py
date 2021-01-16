def selectionSort(lst):
    for i in range(len(lst) - 1):
        min = i
        for j in range(i+1, len(lst), 1):
            if lst[j] < lst[min]:
                min = j
        if min != i:
            lst[i], lst[min] = lst[min], lst[i]
    print(lst)
    return lst

selectionSort([2,0,2,1,1,0])