class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class BinarySearchTree:

    def search(self, node, key):
        if node is None:
            return None
        
        if node.val == key:
            return node
        
        return self.search(node.right, key) if node.val < key else self.search(node.left, key)
    

    def insert(self, root, key):
        if root is None:
            root = Node(key)
        
        else:
            if root.val < key:
                if root.right is None:
                    root.right = Node(key)
                else:
                    self.insert(root.right, key)
            else:
                if root.left is None:
                    root.left = Node(key)
                else:
                    self.insert(root.left, key)


    def inorder(root): 
        if root: 
            self.inorder(root.left) 
            print(root.val) 
            self.inorder(root.right)