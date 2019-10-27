if __name__ == "__main__":
    try:
        while True:
            n = int(input())
            if n==0:
                break
        
            data_obj, max_num, counter = {}, 0,0

            for i in range(n):
                data =[0] * 5
                data[0],data[1],data[2],data[3],data[4] = input().split()
                data[0],data[1],data[2],data[3],data[4] = int(data[0]),int(data[1]),int(data[2]),int(data[3]),int(data[4])
                data.sort()
                res = str(data[0])+str(data[1])+str(data[2])+str(data[3])+str(data[4])

                if res in data_obj:
                    data_obj[res] += 1
                else:
                    data_obj[res]=1

                if max_num < data_obj[res]:
                    max_num = data_obj[res]
                    # print(max_num)
            for num in data_obj:
                if data_obj[num] == max_num:
                    counter += max_num
        
            print(counter)


    except:
        pass