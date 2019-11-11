def game_with_cell(n,m):
    return (n+n%2)*(m+m%2)//4

if __name__ == "__main__":
    n,m = map(int, input().split())
    print(game_with_cell(n,m))
