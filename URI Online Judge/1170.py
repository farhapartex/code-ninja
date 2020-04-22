import decimal

if __name__ == "__main__":
    try:
        test = int(input())

        while test>0:
            weight = decimal.Decimal(input())
            cnt = 0

            while weight > 1:
                weight = weight/2
                if weight > 1:
                    cnt += 1
                else:
                    break
            
            print("{0} dias".format(cnt+1))

            test -= 1
    except:
        pass