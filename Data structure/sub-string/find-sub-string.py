if __name__ == "__main__":
    str = input()
    data = [str[i:j ]for i in range(len(str))
        for j in range(i+1, len(str)+1)]
    
    print(data)