try:
    test = int(input())
    while test >0:
        st = input()
        data, cnt = [], 0
        for ch in st:
            if ch == '<':
                data.append(ch)
            elif ch == '>':
                if '<' in data:
                    cnt += 1
                    del data[-1]
            else:
                continue
        
        print(cnt)
        test -= 1
except:
    pass