# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # step 1: define a helper function called same that checks if the given
        # tree is the same as another tree. It takes in two roots

        def same(p, q):
            if not p and not q: 
                return True
            if not q or not p: 
                return False
            if p.val != q.val: 
                return False
            return same(p.left, q.left) and same(p.right, q.right)

        # step 2: iterate through the main tree using DFS or BFS. Call the 
        # helper function whenever we reach a node that has the same value
        # as the root from the subroot. 

        if not root: 
            return False
        flag = same(root, subRoot)
        if flag:
            return flag
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        

        # keep iterating until you reach the end of the main tree or you find 
        # a subtree that works. 
        