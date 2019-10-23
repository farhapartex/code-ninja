class Solution:
        
    def middleNode(self, head: ListNode) -> ListNode:
        obj1 = head
        obj2 = head
        
        while obj2 and obj2.next:
            obj1 = obj1.next
            obj2 = obj2.next.next
        
        return obj1