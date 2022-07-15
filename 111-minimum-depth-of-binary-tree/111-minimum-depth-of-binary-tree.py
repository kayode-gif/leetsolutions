# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        #iterative dfs 
        
        # if not root:
        #     return 0
        # stack = [(root,1)]
        # curr_depth = float('inf')
        # while stack:
        #     node,depth = stack.pop()
        #     if not node.right and not node.left:
        #         curr_depth = min(curr_depth,depth)
        #     if node.right:
        #         stack.append((node.right,depth+1))
        #     if node.left:
        #         stack.append((node.left,depth+1))
        # return curr_depth
        
        #recursive dfs 
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if not root.left and root.right:
            return 1 + self.minDepth(root.right)
        if not root.right and root.left:
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left),self.minDepth(root.right))
    