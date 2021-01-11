class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        outputArray = []
        onlyArr1 = []
        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr2[i] == arr1[j]:
                    outputArray.append(arr2[i])
        for i in range(len(arr1)):
            if arr1[i] not in arr2:
                onlyArr1.append(arr1[i])
        return outputArray + sorted(onlyArr1)