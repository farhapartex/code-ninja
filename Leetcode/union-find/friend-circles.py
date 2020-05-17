class Solution:
    def __init__(self):
        self.par = []
        
        
    def makeset(self,n):
        self.par[n] = n
        
        
    def find(self,u):
        if self.par[u] == u:
            return u

        self.par[u] = self.find(self.par[u])
        return self.par[u]
    
    
    def union(self,a,b):
        u = self.find(a)
        v = self.find(b)
        if u != v:
            self.par[v] = u
            
            
        
    def findCircleNum(self, M: List[List[int]]):
        self.par = [None] * (len(M)+1)
        res = []
        
        arr_size = len(M)
        
        for i in range(arr_size):
            self.makeset(i)
        
        for i in range(arr_size):
            for j in range(arr_size):
                if M[i][j] == 1:
                    self.union(i,j)
        
        return sum([self.find(i) == i for i in range(arr_size)])
                       