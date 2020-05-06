class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack, ans = [], 0
        for d in ops:
            if d == "C":
                m = stack.pop()
                ans -= m
            else:
                if d == "D":
                    m = stack[-1]*2
                elif d == "+":
                    m = stack[-1] + stack[-2]
                else:
                    m = int(d)
                    
                stack.append(m)
                ans += m
        
        return ans
        