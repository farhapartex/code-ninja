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
    rect1 = [int(n) for n in input().split()]
    rect2 = [int(n) for n in input().split()]

    print(True) if rect1[0] < rect2[2] and rect1[1] < rect2[3] and rect1[2] > rect2[0] and rect1[3] < rect2[1] else print(False)