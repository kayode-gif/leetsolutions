# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #iterative dfs 
        # if not root:
        #     return root 
        # stack = [root]
        # while stack:
        #     node = stack.pop()
        #     node.right,node.left = node.left,node.right
        #     if node.right != None:
        #         stack.append(node.right)
        #     if node.left != None:
        #         stack.append(node.left)
        # return root
    
        #recursive dfs 
        if not root:
            return root
        root.right,root.left = self.invertTree(root.left),self.invertTree(root.right)
        return root
        
        
            
        