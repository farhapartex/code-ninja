def insertNodeAtHead(head, data):
    node = SinglyLinkedListNode(data)
    if head is None:
        head=node
    else:
        temp = head
        head = node
        head.next = temp
    return head
    