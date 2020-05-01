try:
    while True:
        n,m = [int(x) for x in input().split()]
        data = [int(x) for x in input().split()]
        data_dic = {}
        for i in range(n):
            if data[i] not in data_dic:
                data_dic[data[i]] = [i]
            else:
                data_dic[data[i]].append(i)

        while m > 0:
            k, v = [int(x) for x in input().split()]
            if v not in data_dic or len(data_dic[v]) < k or k == 0:
                print(0)
            else:
                print(data_dic[v][k-1] + 1)
            m -= 1
except:
    pass