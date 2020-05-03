class MyStack:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        

    def push(self, x: int):
        """
        Push element x onto stack.
        """
        self.data.append(x)
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.data.pop()
        

    def top(self):
        """
        Get the top element.
        """
        return self.data[-1]
        

    def empty(self):
        """
        Returns whether the stack is empty.
        """
        return False if len(self.data)>0 else True
        