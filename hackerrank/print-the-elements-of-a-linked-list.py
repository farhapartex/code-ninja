def printLinkedList(head):
    if head is None:
        return
    else:
        temp = head
        while temp is not None:
            print(temp.data)
            temp = temp.next