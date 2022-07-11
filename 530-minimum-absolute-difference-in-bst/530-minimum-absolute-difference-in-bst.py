# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        queue = [root]
        res = []
        diff = float('inf')
        val = 0
        while queue:
            node = queue.pop(0)
            res.append(node.val)
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
        res.sort()
        for i in range(len(res)-1):
            if abs(res[i+1] - res[i]) < diff:
                diff = abs(res[i+1] - res[i])
                
        return diff
        
        
            