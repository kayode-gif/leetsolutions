# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root
        queue = [root]
        while queue:
            node = queue.pop(0)
            node.right,node.left = node.left,node.right
            if node.right != None:
                queue.append(node.right)
            if node.left != None:
                queue.append(node.left)
        return root
                    
        
        