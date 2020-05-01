if __name__ == "__main__":
    try:
        while True:
            n,m = [int(x) for x in input().split()]
            if n==0 and m==0:
                break
            data = {}
            for i in range(1,n+1):
                st = input().split()
                data[i] = st[1:]
                
            cnt = 0
            
            for i in range(1,m+1):
                st = input().split()[1:]
                for key in data:
                    for ch in st:
                        if ch in data[key]:
                            cnt += 1
                            break
            
            print(cnt)
                
    except:
        pass