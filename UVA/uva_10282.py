if __name__ == "__main__":
    try:
        data = {}
        while True:
            str = input()
            if str is None or len(str)==0:
                break
            str_list = str.split(" ")
            data[str_list[1]] = str_list[0]
        
        while True:
            str = input()
            if str in data:
                print(data[str])
            else:
                print("eh")
    except:
        pass