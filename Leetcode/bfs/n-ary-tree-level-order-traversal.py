"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        queue, res = deque([root]), []
        
        while queue:
            curr = []
            for i in range(len(queue)):
                node = queue.popleft()
                curr.append(node.val)
                
                for child in node.children:
                    queue.append(child)
                
            res.append(curr)
            
        return res
        