if __name__ == "__main__":
    test = int(input())

    while test > 0:
        data = [int(n) for n in input().split()]
        avg = sum(data[1:])//len(data[1:])
        cnt=0
        for num in data[1:]:
            if num > avg:
                cnt+=1
        res = (100*cnt)/len(data[1:])
        print("{:.3f}%".format(round(res, 3)))

        test -= 1