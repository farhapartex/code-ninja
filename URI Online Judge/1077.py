def infix_to_postfix(expression):
    precedence={'^':5,'*':4,'/':4,'+':3,'-':3,'(':2,')':1}
    stack, ans = [], ""
    for ch in expression:
        if ch == "+" or ch == "-" or ch == "*" or ch == "/" or ch == "^":
            if stack:
                while precedence[ch] <= precedence[stack[-1]]:
                    ans += stack[-1]
                    stack.pop()
                    if not stack:
                        break
            stack.append(ch)
        elif ch == "(":
            stack.append(ch)
        elif ch == ")":
            while stack[-1] != "(":
                ans += stack[-1]
                stack.pop()
            stack.pop()
        else:
            ans += ch
    
    while len(stack) > 0:
        ans += stack[-1]
        stack.pop()
    
    return ans
        

try:
    test = int(input())
    while test > 0:
        exp = input()
        print(infix_to_postfix(exp))
        
        test -= 1
except:
    pass