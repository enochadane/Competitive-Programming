def removeDuplicates(self, nums):
    for i in range(len(nums) - 1):
        j = i + 1
        while j < len(nums) and nums[i] == nums[j]:
            if nums[i] == nums[j]:
                nums.pop(j)
            else:
                j += 1
    
    return len(nums)