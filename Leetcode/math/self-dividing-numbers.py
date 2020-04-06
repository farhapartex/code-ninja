def selfDividingNumbers(left, right):
    payload = []

    for num in range(left, right+1):
        if num%10==0:
            continue
        okay = True
        for s in str(num):
            if int(s) ==0 or num % int(s) != 0:
                okay = False
                break
        if okay:
            payload.append(num)
    
    return payload


if __name__ == "__main__":
    left, right = [int(n) for n in input().split()]
    print(selfDividingNumbers(left, right))