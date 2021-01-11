def checkPossibility(self, nums):
    fail = 0
    failedIndex = -1
    failedJ = -1
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums), 1):
            if nums[i] > nums[j] and i != failedIndex and j != failedJ:
                fail += 1
                failedIndex = i
                failedJ = j
            if fail > 1:
                break
        if fail > 1:
            break
    if fail > 1:
        return False
    return True