skill = input()
skills = list(map(int, input().split()))
skills = sorted(skills)
max_ = 1
l, r = 0, 0
local_max = 0
while r < len(skills):
    if skills[r] - skills[l] <= 5:
        local_max = (r - l) + 1
        r += 1
    else:
        l += 1
        r += 1
        local_max = 0
    max_ = max(max_, local_max)
print(max_)