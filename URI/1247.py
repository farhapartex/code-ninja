import math

if __name__ == "__main__":

    try:
        while True:
            d, vf, vg = [int(n) for n in input().split()]
            x = math.sqrt(d**2+144)
            print("S") if x/vg <= 12/vf else print("N")
    except:
        pass

        