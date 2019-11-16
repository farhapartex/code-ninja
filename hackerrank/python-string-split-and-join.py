def split_and_join(str):
    line = str.split()
    return "-".join(line)

if __name__ == "__main__":
    line = input()
    print(split_and_join(line))