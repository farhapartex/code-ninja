def get_index(data, n):
    idx=0
    while idx < len(data):
        d = data[idx]
        if d == n:
            return idx
        idx += 1

if __name__ == "__main__":
    data = []
    for _ in range(int(input())):
        command, *values = input().split()
        values = list(map(int, values))
        if command == "insert":
            data.insert(values[0],values[1])
        elif command == "print":
            print(data)
        elif command == "remove":
            data.pop(get_index(data, values[0]))
        elif command == "append":
            data.append(values[0])
        elif command == "sort":
            data.sort()
        elif command == "pop":
            data.pop(len(data)-1)
        elif command == "reverse":
            data = data[::-1]

