"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        l = []
        def traverse(root: 'Node'):
            if not root:
                return
            for child in root.children:
                traverse(child)
            l.append(root.val)
        traverse(root)
        return l
        