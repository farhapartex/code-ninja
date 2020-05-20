# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        
        queue, res = deque([root]), []
        
        while queue:
            curr = []
            
            for i in range(len(queue)):
                node = queue.popleft()
                curr.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(curr)
        
        return res[::-1]
        