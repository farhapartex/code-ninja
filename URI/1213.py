try:
    while True:
        n = int(input())
        l, cnt= 1, 1
        while l%n != 0:
            l = (l*10+1)%n
            cnt += 1
        print(cnt)
except:
    pass