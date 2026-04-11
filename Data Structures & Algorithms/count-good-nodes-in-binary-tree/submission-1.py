
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # im thinking DFS for this one?

        # or maybe you can use bfs, keep track of the highest number
        # that you have seen so far. 

        # i think i should use recursion? maybe, you can. Actually, yes,
        # recursion makes sense. You should call it with the new subtree, 
        # where root.val is the best value.

        # base case: 

        count = 0

        stack = [(root, root.val)]

        while stack: 
            node, greatest = stack.pop()

            if node.val >= greatest: 
                count +=1 
            newMax = max(greatest, node.val)
            if node.right: 
                stack.append((node.right, max(newMax, node.right.val)))
            if node.left: 
                stack.append((node.left, max(newMax, node.left.val)))
        return count
            

            


            



            
        
        
                








