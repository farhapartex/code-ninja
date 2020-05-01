if __name__ == "__main__":
    try:
        while True:
            n = int(input())
            if n==0: break
            data = {}
            for i in range(0,n):
                st = input().split()
                data[st[0]] = st[1]
            
            m = int(input())
            if m==0:
                print(0)
                continue
            cnt = 0
            for i in range(0,m):
                st = input().split()
                k=0
                for j in range(0, len(st[1])):
                    if st[1][j] != data[st[0]][j]:
                        k += 1
                if k > 1:
                    cnt += 1
            
            print(cnt)
    except:
        pass