from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
        self.nodes, self.visited,self.route = {}, {}, {}
        self.node=0
    

    def add_edge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def print_path(self,src,des):
        if src==des:
            return
        self.print_path(self.route[src], des)
        print("{0} {1}".format(self.route[src], src))
    

    def bfs(self,s, des):
        queue = []
        queue.append(s)
        self.visited[s] = True

        while queue:
            u = queue.pop(0)

            for v in self.graph[u]:
                if self.visited[v] == False:
                    queue.append(v)
                    self.visited[v] = True
                    self.route[v] = u

                    if des == v:
                        return True
        return False


if __name__ == "__main__":
    try:
        prime=False
        n = input()
        while n!="":
            grp = Graph()
            n = int(n)

            for i in range(n):
                u,v = input().split()
                grp.visited[u]=False
                grp.visited[v]=False
                grp.add_edge(u, v)
            
            src,des = input().split()
            if prime:
                print("")
            prime=True
            if grp.bfs(src,des):
                grp.print_path(des,src)
            else:
                print("No route")
            # print("")
            n = input()
    except:
        pass