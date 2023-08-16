nums = [5,4,-1,7,8]
res = [(0,0)]*len(nums)

if len(nums) == 0:
    print(0)
res = nums[0]
cur_sum = 0
for i in range(len(nums)):
    cur_sum += nums[i]
    if cur_sum > res:
        res = cur_sum
    if cur_sum < 0:
        cur_sum = 0 
print(res)