# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def __init__(self):
    #     self.head = None
        
    def reverseList(self, head: ListNode) -> ListNode:
        prev, next, current = None, None, head
        
        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        
        head = prev
        return head
        