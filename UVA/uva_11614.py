import math

test = int(input())

for i in range(test):
    n = int(input())
    x = int(math.sqrt(1+8*n)) - 1
    print(int(x/2))