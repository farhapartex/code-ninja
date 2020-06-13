class Solution:
    def __init__(self):
        self.data = [1,1]
    

    def fibonacci(self,k):
        for i in range(2,49):
            #print(i)
            self.data.append(self.data[i-1] + self.data[i-2])
            if self.data[-1] >=k:
                break
        
    def findMinFibonacciNumbers(self, k: int) -> int:
        self.fibonacci(k)
        count, index = 0, len(self.data)-1
        while k > 0:
            if self.data[index] <= k:
                k -= self.data[index]
                count += 1
            
            index -= 1
        
        return count