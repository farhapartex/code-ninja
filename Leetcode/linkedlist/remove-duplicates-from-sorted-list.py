# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return
        prev, data, temp = None, [], head
        
        while temp is not None:
            if temp.val in data:
                prev.next = temp.next
                temp = temp.next
            else:
                prev = temp
                data.append(temp.val)
                temp = temp.next
        
        return head
        