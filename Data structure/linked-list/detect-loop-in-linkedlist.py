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
    
    def print_list(self):
        if self.head == None:
            print("Empty Linkedlist")
            return

        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
    
    def detect_loop(self):
        if self.head is None:
            return False

        temp = self.head
        data = []

        while temp is not None:
            if temp.data in data:
                return True
            data.append(temp.data)
            temp = temp.next
        return False



if __name__ == "__main__":
    llist = LinkedList()

    llist.push_front(6)
    llist.push_front(10)
    llist.push_front(6)
    llist.push_front(11)
    llist.push_front(20)

    llist.print_list()

    llist.head.next.next.next = llist.head

    if llist.detect_loop():
        print("Loop Found")
    else:
        print("No Loop")