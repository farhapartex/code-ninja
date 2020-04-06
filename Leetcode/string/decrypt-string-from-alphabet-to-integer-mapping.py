def freqAlphabets(str):
    i, val, res, ans = 0, "", "", ""

    while i< len(str):
        if str[i].isnumeric():
            val += str[i]
            if i == len(str)-1:
                res += "".join([chr(96+int(s)) for s in val])
                val = ""
        elif str[i] == "#" or i == len(str)-1:
            if str[i] == "#":
                ans=""
                ans += chr(96+int(val[-2:]))
                val = val[0:len(val)-2]
                if len(val)>0:
                    res += "".join([chr(96+int(s)) for s in val])
                res = res + ans
            val = ""
        i += 1
    
    return res

if __name__ == "__main__":
    res = freqAlphabets(input())
    print(res)
    
    