class MathRecursion:

    def __init__(self):
        self.F = [0]*38
        self.F[0]=0
        self.F[1]=1
        self.F[2]=1

    def summation(self, n):
        if n == 1:
            return 1
        return n + self.summation(n-1)
    

    def factorial(self, n):
        if n==1:
            return 1
        return n * self.factorial(n-1)
    

    def recursion(self, n):
        if n <= 2:
            return self.F[n]
        elif self.F[n] > 0:
            return self.F[n]
            
        self.F[n-1] = self.recursion(n-1)
        self.F[n-2] = self.recursion(n-2)
        self.F[n-3] = self.recursion(n-3)
        
        return self.F[n-1] + self.F[n-2] + self.F[n-3]

    def tribonacci(self, n: int):
        
        return self.recursion(n)
        


if __name__ == "__main__":
    n = int(input())
    obj = MathRecursion()
    print(obj.tribonacci(n))