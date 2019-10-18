from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def dfs_util(self, u,des, visited):
        visited[u] = True
        print(u, end=" ")

        if u == des:
            self.found=True
            return

        for v in self.graph[u]:
            if self.found:
                return
            if visited[v] == False:
                self.dfs_util(v,des, visited)

    def dfs(self,u,des):
        self.found = False
        visited = [False] * ((len(self.graph))+1)
        print(len(self.graph))
        self.dfs_util(u,des, visited)


g = Graph() 
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,4)
g.add_edge(2,5)
g.add_edge(2,6)
g.add_edge(4,7)
g.add_edge(5,7)
g.add_edge(5,8)
g.add_edge(3,6)
g.add_edge(9,6) 
  
print("Following is DFS from (starting from vertex 2)") 
g.dfs(1,8)