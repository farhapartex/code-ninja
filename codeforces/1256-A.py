q = int(input())

for i in range(q):
    a,b,n,s = map(int, input().split())
    t = (a*n) + (b*1)
    print("YES" if min(s//n,a)*n+b >= s else "NO")  