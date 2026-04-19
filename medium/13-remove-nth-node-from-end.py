class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        
        fast = dummy
        slow = dummy
        
        # move fast pointer n steps
        for _ in range(n):
            fast = fast.next
        
        # move both until fast reaches end
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        # remove node
        slow.next = slow.next.next
        
        return dummy.next
