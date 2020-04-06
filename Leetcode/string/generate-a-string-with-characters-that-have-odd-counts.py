class Solution:
    def generateTheString(self, n: int) -> str:
        if n%2==0:
            data = 'a' * (n-1)
            data += 'b'
            return data
        else:
            data = 'a' * n
            return data
        