if __name__ == "__main__":
    try:
        while True:
            st = input()
            stack, flag = [], True
            for ch in st:
                if ch == "(":
                    stack.append(ch)
                elif ch == ")":
                    if len(stack) > 0:
                        del stack[-1]
                    else:
                        flag = False
                        
            if len(stack) > 0:
                flag = False
            print("correct") if flag  else print("incorrect")
    except:
        pass