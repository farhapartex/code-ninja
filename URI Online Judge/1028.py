def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)


if __name__ == "__main__":
    try:
        test = int(input())

        while test>0:
            a,b = [int(n) for n in input().split()]
            print(gcd(a,b))

            test -= 1
    except:
        pass