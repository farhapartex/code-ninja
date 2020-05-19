"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
    

    def add_edge(self,u,v):
        self.graph[u].append(v)
    

    def bfs(self,s, node,importance_list ):
        visited = [False] * (node + 1)
        queue = []
        importance = importance_list[s]
        queue.append(s)
        visited[s] = True
        # dist[s]=0

        while queue:
            u = queue.pop(0)

            for v in self.graph[u]:
                if visited[v] == False:
                    queue.append(v)
                    visited[v] = True
                    importance += importance_list[v]
        return importance
                    
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = Graph()
        polapain, importance_list, max_id = [], {}, 0
        
        for employee in employees:
            u = employee.id
            if max_id < u:
                max_id = u
            importance_list[u] = employee.importance
            vs = employee.subordinates
            for v in vs:
                graph.add_edge(u,v)
        return graph.bfs(id, max_id, importance_list)
        