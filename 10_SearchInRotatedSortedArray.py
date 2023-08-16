nums = [4,5,6,7,0,1,2]
target = 0
l, r = 0, len(nums) - 1

while l <= r:
    mid = (l+r)//2
    if target == nums[mid]:
        print(mid)
        break

    # left sorted portion:
    if nums[l] <= nums[mid]:
        if target > nums[mid]:
            l = mid + 1
        elif target >= nums[l]:
            r = mid - 1
        else:
            l = mid + 1
    else:
        if target < nums[mid]:
            r = mid - 1
        elif target <= nums[r]:
            l = mid + 1
        else:
            r = mid - 1 
    


    


