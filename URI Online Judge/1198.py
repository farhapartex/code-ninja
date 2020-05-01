if __name__ == "__main__":
    try:
        while True:
            data = [int(n) for n in input().split()]
            res = data[0]-data[1]
            print(res*(-1)) if res<0 else print(res)
    except:
        pass