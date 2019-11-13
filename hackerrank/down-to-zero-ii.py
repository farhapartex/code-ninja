import math

def get_divisor(n):
    limit, flag = int(math.sqrt(n)), False
    while limit >=2:
        if n%limit==0:
            limit = max(limit, int(n/limit))
            flag=True
            break
        limit -= 1
    
    if flag==False: limit=n
    return (limit,flag)

if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        n = int(input())
        queue = []
        while True:
            n, flag = get_divisor(n)
            if flag:
                queue.append(n)
            else:
                n -= 1
                queue.append(n)

            if n==0:
                break
        print(len(queue))