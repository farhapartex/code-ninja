class Solution:
    
    def dec_to_binary(self, n):
        num = ""
        for i in range(63, -1, -1):
            k = n >> i
            num = num + "1" if k & 1 else num + "0"
        
        return num
    
    def hammingDistance(self, x: int, y: int) -> int:
        x = self.dec_to_binary(x)
        y = self.dec_to_binary(y)
        count = 0
        
        for i in range(len(x)):
            if x[i] != y[i]:
                count += 1
        
        return count