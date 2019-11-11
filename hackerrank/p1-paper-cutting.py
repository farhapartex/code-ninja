if __name__ == "__main__":
    m,n = list(map(int,input().split()))
    a = (m-1) + (m*(n-1))
    b = (n-1) + (n*(m-1))
    print(min(a,b))
    