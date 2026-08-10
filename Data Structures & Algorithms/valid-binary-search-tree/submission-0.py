# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def getMin(root):
            if not root:
                return None
            mini = root.val
            lmin, rmin = getMin(root.left), getMin(root.right)
            if lmin is not None:
                mini = min(mini, lmin)
            if rmin is not None:
                mini = min(mini, rmin)
            return mini
        def getMax(root):
            if not root:
                return None
            maxi = root.val
            lmax, rmax = getMax(root.left), getMax(root.right)
            if lmax:
                maxi = max(maxi, lmax)
            if rmax:
                maxi = max(maxi, rmax)
            return maxi
        isValid = self.isValidBST(root.left) and self.isValidBST(root.right)
        lmax = getMax(root.left)
        rmin = getMin(root.right)
        if (lmax is not None and lmax>=root.val) or (rmin is not None and rmin<=root.val):
            return False
        return isValid

        
        