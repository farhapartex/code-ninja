# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, next, current = None, None, head
        
        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        
        return prev
        