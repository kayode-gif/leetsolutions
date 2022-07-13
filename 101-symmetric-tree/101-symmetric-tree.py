# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return Trye
        queue = [(root.left,root.right)]
        while queue:
            nodeL,nodeR = queue.pop(0)
            if nodeL is None and nodeR is None:
                continue 
            if nodeL is None or nodeR is None:
                return False
            if nodeL.val != nodeR.val:
                return False
            queue.append((nodeL.left,nodeR.right))
            queue.append((nodeR.left,nodeL.right))
        return True
                
            
        