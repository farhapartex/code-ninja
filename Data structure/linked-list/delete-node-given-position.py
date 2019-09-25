"""
Given a ‘key’, delete the first occurrence of this key in linked list.
To delete a node from linked list, we need to do following steps.
1) Find previous node of the node to be deleted.
2) Change the next of previous node.
3) Free memory for the node to be deleted.
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
    
    def deleteNodeGivenPosition(self, position):
        if self.head is None:
            return
        temp = self.head

        if position == 0:
            self.head = temp.next 
            temp = None
            return
        
        # Find previous node of the node to be deleted 
        for i in range(position-1):
            temp = temp.next
            if temp is None:
                break
        
        # If position is more than number of nodes 
        if temp is None: 
            return 
        if temp.next is None: 
            return 
        
        # Node temp.next is the node to be deleted 
        # store pointer to the next of node to be deleted 
        next = temp.next.next
        temp.next=None

        # Unlink the node from linked list 
        temp.next = next


if __name__ == "__main__":
    llist = LinkedList()

    llist.append(6)
    llist.push_front(10)
    llist.push_front(6)
    llist.push_front(11)
    llist.append(20)

    llist.insert_after(llist.head.next, 8)

    llist.print_list()

    llist.deleteNodeGivenPosition(2)  
    print("Linked List after Deletion at 2:")
    llist.print_list() 