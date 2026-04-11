class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Step 1: Find the middle of the list
        slow = head
        fast = head
        
        # Move slow one step, fast two steps
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        middle = slow.next
        slow.next = None  # Important: cut the list in half!
        
        # Step 2: Reverse the second half
        prev = None
        curr = middle
        while curr:
            after = curr.next
            curr.next = prev
            prev = curr
            curr = after
        
        # Step 3: Merge the two halves
        first = head
        second = prev  # prev is now the head of reversed second half
        
        while second: 
            temp1 = first.next
            temp2 = second.next
            
            # Reorder
            first.next = second
            second.next = temp1
            
            # Move forward
            first = temp1
            second = temp2