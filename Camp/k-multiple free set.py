k = int(input().split()[1])
nums = list(map(int, input().split()))
nums = sorted(nums)
set_ = set()
for num in nums:
    if num / k in set_:
        continue
    else:
        set_.add(num)
print(len(set_))