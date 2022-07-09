# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        min_sum = 0
        if root == None:
            return 0
        while queue:
            length = len(queue) 
            min_sum +=1
            for neighbours in range(length):
                node = queue.pop(0)
                if node.left == None and node.right == None:
                    return min_sum
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
        return min_sum