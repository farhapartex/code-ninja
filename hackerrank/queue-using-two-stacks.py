class Queue:
    def __init__(self):
        self.first = []
    

    def push(self,x):
        self.first.append(x)
    
    def pop(self):
        self.first = self.first[1:]
    
    def top(self):
        print(self.first[0])


if __name__ == "__main__":
    queue = Queue()
    test = int(input())
    for i in range(test):
        data = list(map(int, input().split()))
        if data[0]==1:
            queue.push(data[1])
        elif data[0]==2:
            queue.pop()
        else:
            queue.top()
