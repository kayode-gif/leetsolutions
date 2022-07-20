# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not subRoot:
            return True
        if not root:
            return False
        if self.isSameTree(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p,q)]
        while stack:
            nodeP,nodeQ = stack.pop()
            if not nodeP and not nodeQ:
                continue 
            if not nodeP or not nodeQ:
                return False
            else:
                if nodeP.val != nodeQ.val:
                    return False
            stack.append((nodeP.left,nodeQ.left))
            stack.append((nodeP.right,nodeQ.right))
        return True