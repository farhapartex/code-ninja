class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    

    def delete_list(self):
        current = self.head

        while current is not None:
            prev = current.next 
            del current.data
            current = prev
        self.head = current
    
    def push_front(self, node):
        new_node = Node(node)
        new_node.next = self.head
        self.head = new_node
    

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
    llist.push_front(10)
    llist.push_front(6)
    llist.push_front(11)
    llist.push_front(20)

    llist.print_list()

    llist.delete_list()  
    llist.print_list() 