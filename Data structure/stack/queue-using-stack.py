"""
A queue can be implemented using two stacks. Let queue to be implemented be q and stacks used to 
implement q be stack1 and stack2. q can be implemented in two ways:
"""

class Queue:
    def __init__(self):
        self.s1=[]
        self.s2=[]
    

    def en_queue(self,x):
        while len(self.s1)!=0:
            self.s2.append(self.s1[-1])
            self.s1.pop()
        self.s1.append(x)

        while len(self.s2)!=0:
            self.s1.append(self.s2[-1])
            self.s2.pop()
    def de_queue(self):
        if len(self.s1) == 0:
            return None
        x = self.s1.pop()
        return x
    
    def show_top(self):
        print(self.s1[-1])


if __name__ == "__main__":
    queue = Queue()
    test = int(input())

    for i in range(test):
        data = list(map(int,input().split()))
        if len(data)==2:
            queue.en_queue(data[1])
        elif data[0]==2:
            queue.de_queue()
        else:
            d = queue.de_queue()
            queue.en_queue(d)
            print(d)