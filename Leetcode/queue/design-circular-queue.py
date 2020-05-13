class MyCircularQueue:
    
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.queue = [None]*k
        self.front = self.rear = -1
        self.size = k

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if (self.rear+1)%self.size == self.front:
            return False
        elif self.front==-1 and self.rear==-1:
            self.front = self.rear = 0
            self.queue[self.rear] = value
        else:
            self.rear = (self.rear+1)%self.size
            self.queue[self.rear] = value
            
        return True
        

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.front == -1:
            return False
        elif self.front == self.rear:
            self.queue[self.front] = None
            self.front = self.rear = -1
        else:
            self.queue[self.front] = None
            self.front = (self.front+1)%self.size
        return True
        

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        return -1 if self.front==-1 else self.queue[self.front]
        

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        return -1 if self.rear == -1 else self.queue[self.rear]
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return True if (self.front == -1 and self.rear==-1) else False
        

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return True if (self.rear+1)%self.size == self.front else False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()