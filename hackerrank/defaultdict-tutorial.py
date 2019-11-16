from collections import defaultdict
if __name__ == "__main__":
    n,m = list(map(int, input().split()))
    A, d = [], defaultdict(list)
    for i in range(1,n+1):
        k = input()
        d[k].append(i)
        A.append(k)
    
    for i in range(m):
        k = input()
        if k in A:
            print(" ".join([str(x) for x in d[k]]))
        else:
            print("-1")
