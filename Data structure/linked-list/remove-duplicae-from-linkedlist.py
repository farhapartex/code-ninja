class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    

    def push_front(self, node):
        new_node = Node(node)
        new_node.next = self.head
        self.head = new_node
    

    def remove_duplicate(self):
        if self.head is None:
            return
        temp = self.head

        data = []
        while temp.next is not None:
            if temp.data == temp.next.data:
                next = temp.next.next
                temp.next = None
                temp.next = next
            else:
                temp = temp.next
    
    def print_list(self):
        if self.head == None:
            print("Empty Linkedlist")
            return

        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == "__main__":
    llist = LinkedList()

    llist.push_front(6)
    llist.push_front(12)
    llist.push_front(12)
    llist.push_front(10)
    llist.push_front(11)
    llist.push_front(11)

    llist.print_list()

    llist.remove_duplicate()

    llist.print_list()