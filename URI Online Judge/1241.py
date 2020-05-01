if __name__ == "__main__":
    try:
        test = int(input())
        while test > 0:
            num1, num2 = input().split()
            if len(num1) < len(num2):
                print("nao encaixa")
            else:
                if num1[-len(num2):] == num2:
                    print("encaixa")
                else:
                    print("nao encaixa")
                    
            test -= 1

    except:
        pass