class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        
        print("")
    
    def push_front(self, node):
        new_node = Node(node)
        new_node.next = self.head
        self.head = new_node
    
    def append(self, new_data):
        new_node =  Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    

    def reverse_linked_list(self):
        prev, next, current = None, None, self.head
        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        
        self.head = prev



if __name__ == "__main__":
    llist = LinkedList()

    llist.append(6)
    llist.append(10)
    llist.append(6)
    llist.append(11)
    llist.append(20)

    llist.print_list()
    llist.reverse_linked_list()
    llist.print_list()