if __name__ == "__main__":
    try:
        test = int(input())
        while test > 0:
            str1, str2 = input().split()
            
            index, result = 0, ""
            max_len = max(len(str1), len(str2))
            while index < max_len:
                if index < len(str1):
                    result +=str1[index]
                
                if index < len(str2):
                    result +=str2[index]
                
                index += 1
            
            print(result)
            test -= 1

    except:
        pass