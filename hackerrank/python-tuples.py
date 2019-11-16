if __name__ == "__main__":
    data = []
    n = int(input())
    data = list(map(int, input().split()))
    print(hash(tuple(data)))
        

