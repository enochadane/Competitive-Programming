def countdown():
    t = int(input())
    for _ in range(t):
        n = int(input())
        digits = input()
        nums = []
        for i in range(len(digits)):
            nums.append(digits[i])
        count = 0
        while digitExists(nums):
            if int(nums[-1]) != 0:
                count += int(nums[-1])
                nums[-1] = '0'
            elif nums[-1] == '0':
                index = findDigit(nums)
                swap(nums, index, -1)
                count += 1
        print(count)

def digitExists(nums):
    for num in nums:
        if num != '0':
            return True
    return False

def findDigit(nums):
    for i in range(len(nums)):
        if nums[i] != '0':
            return i

def swap(nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp

countdown()
