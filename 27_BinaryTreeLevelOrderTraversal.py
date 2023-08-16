def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def Traversal(root, level):
            if root != None:
                if len(res)  < level +1:
                    res.append([])
                res[level].append(root.val)
                Traversal(root.left, level+1)
                Traversal(root.right, level+1)
            else:
                return 
        Traversal(root, 0)
        return res