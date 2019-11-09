class SparseArray:
    def __init__(self):
        self.str, self.queue = {}, []
    
    def input_string(self,n):
        for i in range(n):
            s = input()
            self.str[s] = self.str[s]+1 if s in self.str else 1
    
    def query_string(self,q):
        for i in range(q):
            s = input()
            if s in self.str:
                self.queue.append(self.str[s])
            else:
                self.queue.append(0)
    
    def print_data(self):
        for i in self.queue:
            print(i)

if __name__ == "__main__":
    
    spar = SparseArray()
    n = int(input())
    spar.input_string(n)
    q = int(input())
    spar.query_string(q)
    spar.print_data()
        