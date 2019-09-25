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
    

    def search_data_iteratively(self, key):
        temp = self.head
        if temp is None:
            return None

        count = 0

        while temp is not None:
            if temp.data == key:
                print("Found Data at {0}".format(count+1))
                return 
            temp = temp.next
            count += 1
        if temp is None:
            print("Data not found")
    


    def search_data_rec(self, current, key):
        if current is None:
            return False
        if current.data == key:
            return True

        return self.search_data_rec(current.next, key)
    
    def search_data_r(self, key):
        if self.search_data_rec(self.head, key):
            print("Found")
        else:
            print("Not Found")



if __name__ == "__main__":
    llist = LinkedList()

    llist.push_front(6)
    llist.push_front(10)
    llist.push_front(6)
    llist.push_front(11)
    llist.push_front(20)

    llist.print_list()

    llist.search_data_iteratively(10)
    llist.search_data_r(10)