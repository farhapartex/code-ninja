def insertNodeAtTail(head, data):
    node = SinglyLinkedListNode(data)
    if head is None:
        head = node
    else:
        temp = head
        while temp.next is not None:
            temp = temp.next
        temp.next = node
    return head