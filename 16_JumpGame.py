nums = [2,3,1,1,4]
max_position = nums[0]
for i in range(len(nums)):
    if i > max_position:
        print(False)
    if max_position >= len(nums)-1:
        print(True)
    if i+nums[i] > max_position:
        max_position = i +nums[i]
