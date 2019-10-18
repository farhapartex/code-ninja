class DisjointSet:
    def __init__(self, element):
        self.par = [None] * (element+1)
    
    def makeset(self,n):
        self.par[n] = n

    def find(self,u):
        self.par[u] = self.find(self.par[u])
        return self.par[u]

    def union(self,a,b):
        u = self.find(a)
        v = self.find(b)
        if u != v:
            self.par[u] = v
