# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        p1 = p2 = head
        
        while True:
            if p1.next is not None:
                p1 = p1.next
            else:
                break
            
            if p2.next is not None and p2.next.next is not None:
                p2 = p2.next.next
            else:
                break
            
            if p1 == p2:
                return True
        return False
        