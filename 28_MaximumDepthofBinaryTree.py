class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return max(1+self.maxDepth(root.left), 1+self.maxDepth(root.right))
    