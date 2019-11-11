def show_points(x1,y1,m,n):
    x = (2*m)-x1
    y = (2*n)-y1
    print("{0} {1}".format(x,y))


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        x,y,a,b = map(int, input().split())
        show_points(x,y,a,b)