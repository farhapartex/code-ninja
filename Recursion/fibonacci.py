class Fibonacci:
    def __init__(self):
        self.data = [0] * 49
        self.data[0], self.data[1] = 1, 1
    

    def fibonacci(self,n):

        if n==0 or n==1:
            return self.data[n]
        elif self.data[n]!=0:
            return self.data[n]
        else:
            self.data[n-1] = self.fibonacci(n-1)
            self.data[n-2] = self.fibonacci(n-2)
            self.data[n] = self.data[n-1] + self.data[n-2]

            return self.data[n]


obj = Fibonacci()
obj.fibonacci(48)

print(obj.data)
