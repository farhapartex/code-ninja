from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
    

    def add_edge(self,u,v):
        self.graph[u].append(v)
    

    def bfs(self,s, des):
        visited = [False] * ((len(self.graph))+1)
        queue = []
        dist =[0] * ((len(self.graph))+1)
        queue.append(s)
        visited[s] = True
        dist[s]=0

        while queue:
            u = queue.pop(0)

            for v in self.graph[u]:
                if visited[v] == False:
                    queue.append(v)
                    visited[v] = True
                    dist[v] = dist[u] + 1
                    if v == des:
                        print("Minimum distance: {0}".format(dist[v]))
                        return

if __name__ == "__main__":
    g = Graph()

    g.add_edge(0, 1) 
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 6)
    g.add_edge(3, 5)
    g.add_edge(4, 6)
    g.add_edge(5, 7)
    g.add_edge(2, 4) 
    g.add_edge(6, 7)
    g.bfs(0,6)

    # g = Graph() 
    # g.addEdge(0, 1) 
    # g.addEdge(0, 2) 
    # g.addEdge(1, 2) 
    # g.addEdge(2, 0) 
    # g.addEdge(2, 3) 
    # g.addEdge(3, 3) 
    
    # print ("Following is Breadth First Traversal"
    #                 " (starting from vertex 2)") 
    # g.bfs(2)


