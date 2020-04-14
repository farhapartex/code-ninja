import math, decimal

if __name__ == "__main__":
    PI = decimal.Decimal('3.14159')
    G = decimal.Decimal('9.80665')

    try:
        while True:
            h = decimal.Decimal(input())
            p1, p2 = [int(n) for n in input().split()]
            n = int(input())

            while n>0:
                alpha, v = [decimal.Decimal(p) for p in input().split()]
                alpha = (alpha *PI)/180
                vx, vy = v * decimal.Decimal(math.cos(alpha)), v*decimal.Decimal(math.sin(alpha))
                z = (G*h)/(v**2)
                t = (v/G) * (decimal.Decimal(math.sin(alpha)) + decimal.Decimal(math.sqrt( decimal.Decimal(math.sin(alpha)) **2+(2*z))))
                sx = vx * t

                print("{:.5f} -> DUCK".format(sx)) if sx>= p1 and sx<=p2 else print("{:.5f} -> NUCK".format(sx))
                n -= 1
            
    except:
        pass