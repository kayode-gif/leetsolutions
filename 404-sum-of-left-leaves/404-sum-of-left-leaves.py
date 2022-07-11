# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        queue = [root]
        l_sum = 0
        while queue:
            node = queue.pop(0)
            if node.left != None:
                if not node.left.left and not node.left.right:
                    l_sum += node.left.val
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)       
        return l_sum