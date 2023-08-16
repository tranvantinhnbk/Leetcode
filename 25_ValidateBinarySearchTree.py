










# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         def IsLessThan(root, val):
#             if root == None:
#                 return True
#             if root.val >= val:
#                 return False
#             else:
#                 return IsLessThan(root.left, val) and IsLessThan(root.right, val)

#         def IsGreaterThan(root, val):
#             if root == None:
#                 return True
#             if root.val <= val:
#                 return False
#             else:
#                 return IsGreaterThan(root.left, val) and IsGreaterThan(root.right, val)
        
        
#         if root == None: 
#             return True
#         if IsLessThan(root.left, root.val) == False or IsGreaterThan(root.right, root.val) == False:
#             return False

#         return self.isValidBST(root.left) and self.isValidBST(root.right)