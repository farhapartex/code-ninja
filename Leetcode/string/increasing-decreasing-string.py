def sortString(str):
    result = []
    flag, s = True, list(str)

    while len(s) != 0:
        if flag:
            temp = sorted(set(s))
        else:
            temp = sorted(set(s), reverse=True)
        
        for ch in temp: s.remove(ch)
        result.extend(temp)
        flag = not flag
    
    print(result)
    
    return "".join(result)


if __name__ == "__main__":
    str = input()
    ans = sortString(str)
    print(ans)
