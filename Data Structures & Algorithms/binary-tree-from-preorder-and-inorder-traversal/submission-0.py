# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # base case
        if len(preorder) == 0 or len(inorder) == 0: 
            return None
        rootval = preorder[0]
        split = 0
        while rootval != inorder[split]:
            split += 1
        
        
        root = TreeNode(rootval, self.buildTree(preorder[1:split + 1], inorder[0:split]), self.buildTree(preorder[split+1:], inorder[split+1:]) )
        return root


        

        
