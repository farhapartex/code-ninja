from collections import deque

class TopologicalSort:
    def __init__(self, node):
        self.node = node
        self.edges = [[]] * node
        self.in_degree = [0]*node
        self.q, self.count = deque(), 0
        self.sort_data = []
    

    def create_edge(self,a,b):
        self.in_degree[b] += 1
        self.edges[a].append(b)
    
    def create_queue(self):
        for node in range(self.node):
            if self.in_degree[node] == 0:
                self.q.append(node)
    
    def dfs_topology(self):
        self.create_queue()
        while self.q:
            print(self.q)
            u = self.q.popleft()
            self.sort_data.append(u)
            self.count += 1
            for v in self.edges[u]:
                self.in_degree[v] -= 1
                if self.in_degree[v] == 0:
                    # self.sort_data.append(v)
                    self.q.append(v)
        
        return self.sort_data


if __name__ == "__main__":
    node, edge = list(map(int, input().split()))
    topo = TopologicalSort(node)
    for i in range(edge):
        u,v = list(map(int, input().split()))
        topo.create_edge(u,v)
    res = topo.dfs_topology()
    print(res)
