import math

if __name__ == "__main__":
    l,s1,s2 = list(map(int, input().split()))
    for _ in range(int(input())):
        q = int(input())
        d = (l-math.sqrt(q))*math.sqrt(2)/abs(s1-s2)
        print("{0:.4f}".format(d))