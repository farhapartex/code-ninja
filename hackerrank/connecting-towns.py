if __name__ == "__main__":
    test = int(input())
    for i in range(test):
        n = int(input())
        data = list(map(int, input().split()))
        tot=1
        for d in data:
            tot *= d
        print(tot%1234567)