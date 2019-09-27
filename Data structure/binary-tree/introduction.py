"""
A tree whose elements have at most 2 children is called a binary tree. Since each element in a binary 
tree can have only 2 children, we typically name them the left and right child.

** The maximum number of nodes at level ‘l’ of a binary tree is 2(l)-1. (2(l) => 2 to the power of l+1)
** In a Binary Tree with N nodes, minimum possible height or minimum number of levels is => Log2(N+1) 
"""

class Node:
    """docstring for Node."""
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
        