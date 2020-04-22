if __name__ == "__main__":
    test = int(input())

    while test > 0:
        st = input()
        n = int(input())

        ch = ""

        for s in st:
            num = ord(s) - n
            if num < 65:
                num = 90-(65-num)+1
            ch += chr(num)
        print(ch)
        test -= 1