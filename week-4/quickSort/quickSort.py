from random import randint

# def createArray(size = 10, max = 50):
#     return [randint(0, max) for _ in range(size)]

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    smaller, equal, larger = [], [], []
    pivot = arr[-1]
    for el in arr:
        if el < pivot:
            smaller.append(el)
        elif el == pivot:
            equal.append(el)
        else:
            larger.append(el)

    return quickSort(smaller) + quickSort(equal) + quickSort(larger)

a = [6,5,4,3,2,1]
print("before sort", a)
s = quickSort(a)
print("after sort", s)