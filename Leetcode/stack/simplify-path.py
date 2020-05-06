import re

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack, path = [], re.split("/+", path)
        
        for item in path:
            if item == "..":
                if stack:
                    stack.pop()
            elif item != "." and item != "":
                stack.append(item)
        
        res = ""
        while stack:
            res = "/" + stack.pop() + res
            
        return res if res else "/"
        
        