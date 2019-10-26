def get_ascii_value(str):
    num, hx =0, 128
    for i in range(1,len(str)):
        if str[i] != ".":
            if str[i] == "o":
                num += hx
            hx = int(hx / 2) 
    
    return num

if __name__ == "__main__":
    try:
        str = input()
        while True:
            str = input()
            if str[0] == "_":
                break
            ascii_value = get_ascii_value(str)
            print(chr(ascii_value), end="")
    except:
        pass