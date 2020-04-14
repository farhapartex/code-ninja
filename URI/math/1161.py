import decimal

def factorial(num):
    return 1 if (num==0 or num==1) else num * factorial(num-1)

if __name__ == "__main__":
    try:
        while True:
            a,b = [int(n) for n in input().split()]

            print(factorial(a) + factorial(b))

    except:
        pass