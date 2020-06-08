from collections import defaultdict

class KruskalMst:
    def __init__(self,node):
        self.node = node
        self.graph = []
        self.parent = [None] * (node+1)
        self.cost=0
    
    def add_edge(self,u,v,w):
        self.graph.append([u,v,w])

    def make_par(self,n):
        self.parent[n] = n
    
    def find(self,u):
        return u if self.parent[u] == u else self.find(self.parent[u])
    
    def kruskal(self):
        result = []
        count = 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        
        for n in range(1,self.node+1):
            self.make_par(n)

        for g in self.graph:
            u = self.find(g[0])
            v = self.find(g[1])
            if u != v:
                self.parent[u] = v
                count += 1
                self.cost += g[2]

                if count == (node-1):
                    break
        return self.cost

if __name__ == "__main__":
    node,edge = [int(i) for i in input().split()]

    mst = KruskalMst(node)

    for i in range(edge):
        u ,v,w = [int(i) for i in input().split()]
        mst.add_edge(u,v,w)
    

    print(mst.kruskal())
        

    
    