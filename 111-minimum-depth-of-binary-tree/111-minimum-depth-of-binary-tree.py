# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        if root.left==None and root.right==None:
            return 1
        
        global_min=100001       #As max no. of nodes can be 10^5
        if root.left:
            global_min=min(self.minDepth(root.left),global_min)
        if root.right:
            global_min=min(self.minDepth(root.right),global_min)
        
        return global_min+1
                    
                
        