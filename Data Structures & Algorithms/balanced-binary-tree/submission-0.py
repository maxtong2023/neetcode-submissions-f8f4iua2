# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # I think i should find the height of the subtrees
        if not root:
            return True
        # height just finds the height, it can't return a bool
        def height(node):
            if not node: 
                return 0

            right = height(node.right)
            left = height(node.left)

            if left == -1 or right == -1:
                return -1
            if abs(right - left) > 1:
                return - 1
            else: 
                return 1 + max(right, left)
        if height(root) == - 1:
            return False
        else:
            return True
        