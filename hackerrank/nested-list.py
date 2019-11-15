if __name__ == "__main__":
    data = {}
    for _ in range(int(input())):
        name = input()
        num = float(input())
        if num in data:
            data[num].append(name)
        else:
            data[num] = [name]
    numbers = sorted(data.keys())
    names = sorted(data[numbers[1]])
    for i in names:
        print(i)