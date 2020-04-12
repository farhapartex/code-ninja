# -*- coding: utf-8 -*-

if __name__ == "__main__":
    try:
        while True:
            num = input()
            if num[0] == '-':
                break
            if num.isdigit():
                n = hex(int(num))
                print(n[:2] + n[2:].upper())
            else:
                print(int(num,0))
    except:
        pass