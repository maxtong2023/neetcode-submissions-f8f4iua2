# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        head = dummy
        carry = 0

        while l1 and l2: 
            dummy.next = ListNode()
            dummy = dummy.next
            sums = l1.val + l2.val + carry
            carry = 0
            if sums >= 10: 
                sums -= 10
                carry = 1
            dummy.val = sums
            l1 = l1.next
            l2 = l2.next
        while l1: 
            dummy.next = ListNode()
            dummy = dummy.next
            l1.val += carry
            carry = 0
            if l1.val >= 10: 
                l1.val -= 10
                carry = 1
            dummy.val = l1.val
            l1 = l1.next
        while l2: 
            dummy.next = ListNode()
            dummy = dummy.next
            l2.val += carry
            carry = 0
            if l2.val >= 10: 
                l2.val -= 10
                carry = 1
            dummy.val = l2.val
            l2 = l2.next
        print(carry)
        if carry == 1: 
            dummy.next = ListNode(1, None)
            dummy = dummy.next
        return head.next
            
