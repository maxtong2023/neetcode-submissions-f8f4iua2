# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # run dfs through each. If the stacks are different at any point, they should not be the same?

        if not q and not p:
            return True
        if not q or not p: 
            return False
        if q.val != p.val:
            return False

        return self.isSameTree(q.right, p.right) and self.isSameTree(q.left, p.left)
        


        
