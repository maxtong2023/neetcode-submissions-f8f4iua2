from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # just BFS?

        queue = deque()
        queue.append(root)
        result = []
        build = deque()

        if not root: 
            return []


        while queue: 
            build = deque()
            for i in range(len(queue)): 
                node = queue.popleft()
                build.appendleft(node.val)
                if node.right: 
                    queue.append(node.right)
                if node.left: 
                    queue.append(node.left)
            result.append(build)
        return result



