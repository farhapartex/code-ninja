if __name__ == "__main__":
    try:
        while True:
            h1, m1, h2, m2 = [int(x) for x in input().split()]
            if h1==0 and m1==0 and h2==0 and m2==0:
                break
            a = (h1*60) + m1
            b = (h2*60)+m2

            if a<=b:
                print(b-a)
            else:
                a = (12*60) - (((h1-12)*60)+m1)
                print(b+a)
    except:
        pass