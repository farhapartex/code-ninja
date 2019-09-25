"""
A node can be added in three ways
1) At the front of the linked list
2) After a given node.
3) At the end of the linked list.
"""

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
            print(temp.data)
            temp = temp.next
    
    def push_front(self, node):
        new_node = Node(node)
        new_node.next = self.head
        self.head = new_node
    
    def insert_after(self, prev_node, new_node):
        if prev_node is None:
            print("Previous node must be in a LinkedList")
            return
        new_node = Node(new_node)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        new_node =  Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node 


if __name__ == "__main__":
    llist = LinkedList()

    llist.append(6)
    llist.push_front(10)
    llist.push_front(6)
    llist.push_front(11)
    llist.append(20)

    llist.insert_after(llist.head.next, 8)

    llist.print_list()

