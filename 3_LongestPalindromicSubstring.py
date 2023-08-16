### Cach 1
# nums = [-1,0,1,2,-1,-4]
# nums = sorted(nums)
# res = set()
# i = -1
# while i < len(nums) - 1:
#     i+=1
#     if i > 0 and nums[i] == nums[i-1]:
#         continue
#     j = i + 1 
#     k = len(nums) - 1
#     while j < k:
#         if nums[i] + nums[j] + nums[k] < 0:
#             j+=1
#         elif nums[i] + nums[j] + nums[k] > 0:
#             k-=1
#         else:
#             res.add((nums[i], nums[j], nums[k]))
#             j += 1
        
# print(res)
    
### Cach 2
# nums = sorted(nums)
# res = set()
# for i in range(len(nums)):
#     if i > 0 and nums[i] == nums[i-1]:
#         continue
#     j = i + 1 
#     k = len(nums) - 1
#     while j < k:
#         if nums[i] + nums[j] + nums[k] < 0:
#             j+=1
#         elif nums[i] + nums[j] + nums[k] > 0:
#             k-=1
#         else:
#             res.add(((nums[i], nums[j], nums[k])))
#             j += 1
# return res

##Cach 3
# nums = [-1,0,1,2,-1,-4]
# nums = sorted(nums)
# res = set()
# for i in range(len(nums)):
#     if i > 0 and nums[i] == nums[i-1]:
#         continue
#     k = len(nums) - 1
#     for j in range(i+1, len(nums)):
#         if j >= k: 
#             break
#         if nums[i] + nums[j] + nums[k] > 0:
#             k-=1
#         if nums[i] + nums[j] + nums[k] == 0:
#             res.add((nums[i], nums[j], nums[k]))
# print(res)

