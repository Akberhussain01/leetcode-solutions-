class Solution:
    def reverseKGroup(self, head, k):
        
        # Step 1: check if k nodes exist
        count = 0
        temp = head
        while temp and count < k:
            temp = temp.next
            count += 1
        
        # If less than k nodes → return as it is
        if count < k:
            return head
        
        # Step 2: reverse k nodes
        prev = None
        curr = head
        
        for _ in range(k):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # Step 3: recursive call for remaining list
        head.next = self.reverseKGroup(curr, k)
        
        return prev
