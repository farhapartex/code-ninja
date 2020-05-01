if __name__ == "__main__":
    try:
        n,m = [int(x) for x in input().split()]
        data = {}
        while n >0:
            name, amount = input().split()
            data[name] = int(amount)
            n -= 1
        
        while m > 0:
            total = 0
            while True:
                st = input().split()
                if st[0] == ".":
                    print(total)
                    break
                for ch in st:
                    if ch in data:
                        total += data[ch]
            
            m -= 1
    except:
        pass