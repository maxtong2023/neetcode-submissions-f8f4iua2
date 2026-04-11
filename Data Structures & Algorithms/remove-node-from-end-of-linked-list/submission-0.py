# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # step 1, first find the length of the linked list. 
        curr = head
        length = 0

        # subcase, if n = 1, just pop the last node off from the end of the list
        while curr: 
            curr = curr.next
            length += 1
        
        target = length - n # the nth node that we want to remove
        curr = head

        if target == 0:
            return head.next
        # step 2, iterate to the nth node and point it to the node after it.
        for i in range(target - 1):
            curr = curr.next
        
        curr.next = curr.next.next
        return head
        

        