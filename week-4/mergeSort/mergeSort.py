def merge(lst1, lst2):
    merged = []
    i, j = 0, 0
    while len(lst1) > i and len(lst2) > j:
        if lst1[i] < lst2[j]:
            merged.append(lst1[i])
            i += 1
        else:
            merged.append(lst2[j])
            j += 1
    if len(lst1) == i:
        merged += lst2[j:]
    else:
        merged += lst1[i:]
    return merged

def mergeSort(arr):
    if len(arr) == 1:
        return arr
    left, right = mergeSort(arr[:len(arr)//2]), mergeSort(arr[len(arr)//2:])

    return merge(left, right)


print(mergeSort([5,4,3,2,1]))

