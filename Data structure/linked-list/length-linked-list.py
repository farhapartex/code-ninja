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
    

    def get_count_rec(self,head):
        if head is None:
            return 0
        return 1 + self.get_count_rec(head.next)
    
    def get_count(self):
        return self.get_count_rec(self.head)
    
    def get_count_iteratively(self):
        if self.head is None:
            return
        current = self.head
        count=0
        while current is not None:
            current = current.next
            count +=1

        return count 


if __name__ == "__main__":
    llist = LinkedList()

    llist.push_front(6)
    llist.push_front(10)
    llist.push_front(6)
    llist.push_front(11)
    llist.push_front(20)

    print("Length by recursively: {0}".format(llist.get_count()))
    print("Length by iteratively: {0}".format(llist.get_count_iteratively()))

