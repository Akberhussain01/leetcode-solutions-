import heapq

class Solution:
    def mergeKLists(self, lists):
        heap = []
        
        # Step 1: add first nodes
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
        
        dummy = ListNode(0)
        current = dummy
        
        # Step 2: process heap
        while heap:
            val, i, node = heapq.heappop(heap)
            
            current.next = node
            current = current.next
            
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next
