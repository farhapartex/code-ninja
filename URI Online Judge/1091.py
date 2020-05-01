if __name__ == "__main__":
    try:
        while True:
            test = int(input())
            if test == 0: break
            x,y = [int(n) for n in input().split()]
            while test > 0:
                a,b = [int(n) for n in input().split()]
                if x==a or y == b:
                    print("divisa")
                elif x<a and y<b:
                    print("NE")
                elif x<a and y>b:
                    print("SE")
                elif x>a and y>b:
                    print("SO")
                elif x>a and y<b:
                    print("NO")
                
                test -= 1
    except:
        pass