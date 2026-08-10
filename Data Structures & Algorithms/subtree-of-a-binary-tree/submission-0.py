# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, root1, root2):
        if not root1 and not root2:
            return True
        elif not root1 or not root2:
            return False
        return root1.val == root2.val and self.isSameTree(root1.left, root2.left) and self.isSameTree(root1.right, root2.right)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        res = [False]
        def dfs(root):
            if not root:
                return 
            if root.val == subRoot.val and self.isSameTree(root, subRoot):
                res[0] = True
            else:
                dfs(root.left)
                dfs(root.right)
        if not subRoot:
            return True
        dfs(root)
        return res[0]   