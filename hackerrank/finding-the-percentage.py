if __name__ == "__main__":
    avg_marks = {}
    for _ in range(int(input())):
        name, *line = input().split()
        scores = list(map(float, line))
        avg = sum(scores)/3
        avg_marks[name] = avg
    name = input()
    print("{0:.2f}".format(avg_marks[name]))