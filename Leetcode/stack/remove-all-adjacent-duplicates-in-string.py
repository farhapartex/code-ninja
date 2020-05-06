class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for ch in S:
            if len(stack)==0 or stack[-1] != ch:
                stack.append(ch)
            elif stack[-1] == ch:
                stack.pop()
                
        return "".join(stack)