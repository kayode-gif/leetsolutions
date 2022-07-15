# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #recursive dfs
        if not root:
            return 0
        if not root.right and not root.left:
            return 1
        if not root.right and root.left:
            return 1 + self.maxDepth(root.left)
        if not root.left and root.right:
            return 1 + self.maxDepth(root.right)
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
        
        