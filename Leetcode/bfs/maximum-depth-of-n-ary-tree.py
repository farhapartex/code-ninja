"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import defaultdict
    

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        stack = []
        if root: stack.append((root,1))
        depth = 0
        while stack:
            (node, d) = stack.pop()
            depth = max(depth,d)
            for child in node.children:
                stack.append((child,d+1))
        
        return depth
        
        
