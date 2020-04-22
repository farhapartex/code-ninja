if __name__ == "__main__":
    try:
        while True:
            num1, num2 = [bin(int(n))[2:] for n in input().split()]
            if len(num1) > len(num2):
                for i in range(1, (len(num1)-len(num2))+1):
                    num2 = '0' + num2
            elif len(num1) < len(num2):
                for i in range(1, (len(num2)-len(num1))+1):
                    num1 = '0' + num1
            
            res = '0'

            for i in range(0, len(num1)):
                if num1[i] == '0' and num2[i] == '0':
                    res +='0'
                elif (num1[i] == '0' and num2[i] == '1') or (num1[i] == '1' and num2[i] == '0'):
                    res += '1'
                elif num1[i] == '1' and num2[i] == '1':
                    res += '0'
            
            print(int(res,2))
    except:
        pass

