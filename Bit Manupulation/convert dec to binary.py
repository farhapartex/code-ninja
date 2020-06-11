def binary_to_dec(n):
    num, flag = "", False
    for i in range(63, -1, -1):
        k = n>>i
        if k&1:
            num += "1"
            flag = True
        else:
            if flag:
                num += "0"

    return num


if __name__ == "__main__":
    n = int(input())
    print(binary_to_dec(n))