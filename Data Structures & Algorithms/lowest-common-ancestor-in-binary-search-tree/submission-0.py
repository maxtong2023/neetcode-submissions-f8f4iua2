# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        # there are 3 cases. p and q are both less than the current node meaning
        # we should recurse of the curr.left node.
        
        if ((p.val >= root.val and q.val <= root.val) or (p.val <= root.val and q.val >= root.val)):
            return root

        # p and q are both greater than the current node, meaning we should
        # recurse with the curr.right node.

        if (p.val < root.val and q.val < root.val): 
            return self.lowestCommonAncestor(root.left, p, q)

        # p and q are split on the node, meaning that the current node is the 
        # LCA
        else:
            return self.lowestCommonAncestor(root.right, p, q)
