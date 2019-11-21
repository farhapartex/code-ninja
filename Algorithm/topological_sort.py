from collections import defaultdict

class TopologicalSort:
    def __init__(self,node):
        self.node = node
        self.graph = defaultdict(list)
    

    def add_edge(self,u,v):
        self.graph[u].append(v)
    

    def topological_sort_util(self,u,visited,stack):
        visited[u] = True

        for v in self.graph[u]:
            if visited[v] == False:
                self.topological_sort_util(v,visited,stack)
        

        stack.insert(0, u)
    

    def topological_sort(self):
        visited = [False] * self.node
        stack = []

        for u in range(self.node):
            if visited[u] == False:
                self.topological_sort_util(u,visited,stack)
        
        print(stack)



if __name__ == "__main__":
    g = TopologicalSort(2)

    # g.add_edge(5, 2)
    # g.add_edge(5, 0)
    # g.add_edge(4, 0)
    # g.add_edge(4, 1)
    # g.add_edge(2, 3)
    # g.add_edge(3, 1)

    g.add_edge(0, 1)
    g.add_edge(1, 0)

    g.topological_sort()

