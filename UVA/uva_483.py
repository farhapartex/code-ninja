if __name__ == "__main__":
    try:
        while True:
            str = input()
            data = str.split(" ")
            res = ""
            for i in range(len(data)):
                res += data[i][::-1]
                if i< len(data)-1:
                    res += " "
        
            print(res)
    except:
        pass

