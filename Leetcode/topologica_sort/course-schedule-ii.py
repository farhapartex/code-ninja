from collections import deque

class Solution:
    def create_edge(self,in_degree,edges,edge):
        in_degree[edge[0]] += 1
        edges[edge[1]].append(edge[0])
    
    def create_queue(self,nodes,in_degree,queue):
        for n in range(nodes):
            if in_degree[n]==0:
                queue.append(n)
    
    def topology(self,queue,edges,in_degree,nodes):
        res, count = [], 0
        while queue:
            u = queue.popleft()
            count += 1
            res.append(u)
            for v in edges[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
        return res if count == nodes else []
        
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges = [[] for i in range(numCourses)]
        inDegree = [0 for i in range(numCourses)]
        
        for edge in prerequisites:
            self.create_edge(inDegree,edges,edge)
            
        q, count = deque(), 0
        self.create_queue(numCourses,inDegree,q)
        
        return self.topology(q,edges,inDegree,numCourses)