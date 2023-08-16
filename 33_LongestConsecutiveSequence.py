












# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         set_nums = set(nums)
#         res = 0
#         for val in nums:
#             if val in set_nums:
#                 cur_max = 0
#                 i =  val
#                 # Check foward consecutive
#                 while i in set_nums:
#                     cur_max +=1
#                     set_nums.remove(i)
#                     i+=1
#                 i = val-1
#                 #Check backward
#                 while i in set_nums:
#                     cur_max +=1 
#                     set_nums.remove(i)
#                     i-=1
#                 res = max(cur_max, res)
#         return res







