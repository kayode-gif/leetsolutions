# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        #iterative dfs 
        # if not root:
        #     return False
        # stack = [(root,targetSum - root.val)]
        # while stack:
        #     node,value = stack.pop()
        #     if not node.left and not node.right and value == 0:
        #         return True
        #     if node.left != None:
        #         stack.append((node.left,value - node.left.val))
        #     if node.right != None:
        #         stack.append((node.right,value - node.right.val))
        # return False
    
        #recursive dfs 
        if not root:
            return False
        if root.left == None and root.right == None:
            return root.val == targetSum
        return self.hasPathSum(root.left,targetSum - root.val) or self.hasPathSum(root.right,targetSum - root.val)
            
            
        
        
        