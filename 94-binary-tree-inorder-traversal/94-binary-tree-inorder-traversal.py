# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            if node:
                stack.append(node.right)
                stack.append(node)
                stack.append(node.left)
            else:
                if stack:
                    node = stack.pop()
                    result.append(node.val)
        return result
        