# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def dfs(node):
            if not node:
                return 0
            # recursively call left and right childs
            left = dfs(node.left)
            right = dfs(node.right)
            nonlocal diameter
            diameter = max(diameter, left + right)
            return 1 + max(left,right)
        dfs(root)
        return diameter