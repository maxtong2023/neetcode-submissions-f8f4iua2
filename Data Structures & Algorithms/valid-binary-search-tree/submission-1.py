# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # store a tuple for each node on the stack?

        stack = [(root, float("-inf"), float("inf"))]

        while stack: 
            node, lowerbound, upperbound = stack.pop()
            if node.val <= lowerbound or node.val >= upperbound: 
                return False
            if node.right: 
                stack.append((node.right, node.val, upperbound))
            if node.left: 
                stack.append((node.left, lowerbound, node.val))
        return True
        