class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack, right, left, ans = [], 0, 0, ""
        for ch in S:
            if ch == "(":
                stack.append(ch)
                left += 1
            elif ch == ")":
                right += 1
                stack.append(ch)
                if right == left:
                    ans += "".join(stack[1:len(stack)-1])
                    stack, right, left = [], 0, 0
        return ans
        