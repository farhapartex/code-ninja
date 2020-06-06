"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def tree_traverse(self, node, stack):
        if node is None:
            return stack
        
        if node.children is None:
            stack.append(node.val)
            return stack
        
        for child in node.children:
            stack = self.tree_traverse(child, stack)
        
        stack.append(node.val)
        
        return stack
    
    def postorder(self, root: 'Node') -> List[int]:
        return self.tree_traverse(root, [])
        