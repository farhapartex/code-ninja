# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bfs(self, root):
        queue, data = [root], []
        
        while queue:
            if queue == [None]*len(queue):
                break
            u = queue.pop(0)
            if u is None:
                data.append(None)
                continue
            data.append(u.val)
            
            queue.append(u.left)
            queue.append(u.right)
        
        return data
    
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        
        data1 = self.bfs(p)
        data2 = self.bfs(q)
        
        return True if data1 == data2 else False
        