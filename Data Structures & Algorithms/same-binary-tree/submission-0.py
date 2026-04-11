# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # run dfs through each. If the stacks are different at any point, they should not be the same?

        stackp = [p]
        stackq = [q]

        while stackp and stackq: 
            nodep = stackp.pop()
            nodeq = stackq.pop()
            
            if nodeq and not nodep: 
                return False
            elif nodep and not nodeq: 
                return False
            elif not nodep and not nodeq: 
                continue
            
            

            if nodep.val != nodeq.val:
                return False
            stackq.append(nodeq.right)
            stackp.append(nodep.right)
            stackq.append(nodeq.left)
            stackp.append(nodep.left)
        if stackp or stackq: 
            return False
        return True

        
