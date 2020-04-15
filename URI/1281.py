import decimal

if __name__ == "__main__":
    try:
        test = int(input())
        data = {}
        while test >0:
            m = int(input())
            while m > 0:
                st = input().split()
                data[st[0]] = float(st[1])
                m -= 1
            
            p = int(input())
            total = 0.0
            while p > 0:
                st = input().split()
                total += (data[st[0]] * float(st[1]))
                p -= 1
            
            print("R$ {:.2f}".format(total))
            
            test -= 1
    except:
        pass