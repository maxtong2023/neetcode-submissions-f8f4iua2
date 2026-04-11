# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # perhaps you can achieve this with two pointers? one fast and one slow

        slow = head
        fast = head
        odd = False
        while fast:
            if odd: 
                slow = slow.next
            fast = fast.next
            if slow == fast: 
                return True
            odd = not odd
        return False