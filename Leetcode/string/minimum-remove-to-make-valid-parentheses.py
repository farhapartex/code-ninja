class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        index, stack = 0, []
        
        while index < len(s):
            if s[index] == "(":
                stack.append(index)
                index += 1
            elif s[index] == ")":
                if len(stack)>0:
                    stack.pop()
                    index += 1
                else:
                    s = s[:index] + s[index+1:]
            else:
                index += 1
                
        if len(stack)>0:
            index=0
            for idx, index in enumerate(stack):
                s = s[:index-idx] + s[index-idx+1:]
                    
        return s
                
                
            
        