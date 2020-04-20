if __name__ == "__main__":
    try:
        test = int(input())
        while test>0:
            m = int(input())
            data = [int(x) for x in input().split()]
            temp = sorted(data, reverse=True)
            cnt = 0
            
            for i in range(0, len(data)):
                if data[i] == temp[i]:
                    cnt += 1
            
            print(cnt)
            
            test -= 1
                
    except:
        pass