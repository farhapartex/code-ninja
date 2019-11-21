if __name__ == "__main__":
    n = int(input())
    tank, pump = 0, 0
    for i in range(n):
        pert, dis = list(map(int, input().split()))
        tank += (pert - dis)
        if tank <0:
            pump = i+1
            tank = 0
    print(pump)