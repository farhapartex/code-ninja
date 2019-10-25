class RecentCounter(object):
    
    def __init__(self):
        self.data = []
        

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.data.insert(0,t)
        
        while t-3000 > self.data[-1]:
            self.data.pop()
        
        return len(self.data)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)