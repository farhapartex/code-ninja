import math

def is_prime(n):
    if n<=1:
        return False
    if n==2:
        return True
    if n>2 and n%2==0:
        return False
    max_div = math.floor(math.sqrt(n))
    for i in range(3, max_div+1,2):
        if n%i==0:
            return False
    return True


if __name__ == "__main__":
    try:
        test = int(input())

        while test>0:
            num = int(input())
            print("Prime") if is_prime(num) else print("Not Prime")
            test -= 1
    except:
        pass