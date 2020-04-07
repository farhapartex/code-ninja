if __name__ == "__main__":
    try:
        flag=0
        while True:
            test = int(input())
            data = []
            if test == 0: break
            if flag==1:
                print("")

            for i in range(0,test):
                data.append(input())
            
            mx_len = max([len(st) for st in data])
            
            for d in data:
                print("{0}".format( " "*(mx_len-len(d))+d ))
            
            flag=1
            
    except:
        pass