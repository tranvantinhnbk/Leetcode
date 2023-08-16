nums = [2,7,11,15]
memo = {}
target = 9
for idx, num in enumerate(nums):
    if target - num not in memo:
        memo[num] = idx
    else:
        print([memo[target - num], idx])
print(None)
    
