class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        oldToNew = {}

        # First pass: create all new nodes
        curr = head
        while curr:
            oldToNew[curr] = Node(curr.val)
            curr = curr.next
        
        # Second pass: assign next and random pointers
        curr = head
        while curr:
            newNode = oldToNew[curr]
            newNode.next = oldToNew.get(curr.next)
            newNode.random = oldToNew.get(curr.random)
            curr = curr.next
        
        return oldToNew[head]
