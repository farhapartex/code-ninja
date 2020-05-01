if __name__ == "__main__":
    try:
        flag = False
        while True:
            year = input()
            if flag:
                print("")
            flag = True

            le = f = m4 = m15 = m55 = m100 = m400 = 0
            for ch in year:
                m4 = ((m4 * 10) + (ord(ch) - ord('0'))) % 4
                m15 = ((m15 * 10) + (ord(ch) - ord('0'))) % 15
                m55 = ((m55 * 10) + (ord(ch) - ord('0'))) % 55
                m100 = ((m100 * 10) + (ord(ch) - ord('0'))) % 100
                m400 = ((m400 * 10) + (ord(ch) - ord('0'))) % 400

            if m4 == 0 and m100 != 0 or m400 == 0:
                print("This is leap year.")
                le = f = 1
            
            if m15 == 0:
                print("This is huluculu festival year.")
                f = 1
            
            if le == 1 and m55 == 0: print("This is bulukulu festival year.")
            if f == 0: print("This is an ordinary year.")
    except:
        pass