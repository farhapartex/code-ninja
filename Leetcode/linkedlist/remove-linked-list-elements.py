# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return
        
        temp = ListNode(0)
        temp.next = head
        node = temp
        
        while node.next is not None:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next
        return temp.next
        