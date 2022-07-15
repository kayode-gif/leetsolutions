# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #recursive dfs 
        # if no nodes, then its true
        # if not p and not q:
        #     return True
        # if not p or not q:
        #     return False
        # if p.val != q.val:
        #     return False
        # return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
    
        #iterative dfs 
        stack = [(p,q)]
        while stack:
            nodeP,nodeQ = stack.pop()
            if nodeP == None and nodeQ == None:
                continue 
            elif nodeP == None or nodeQ == None:
                return False
            else:
                if nodeP.val != nodeQ.val:
                    return False
                stack.append((nodeP.left,nodeQ.left))
                stack.append((nodeP.right,nodeQ.right))
        return True
    
    
        