if __name__ == "__main__":
    try:
        while True:
            st = input()
            if st == "":
                print("")
                continue

            data = sorted(list(set([ord(ch) for ch in st.replace(" ", "")])))
            start, index, res = data[0], 0, []
            if index == len(data):
                print("{0}:{1}".format(chr(start), chr(start)))
                continue

            while True:
                if index+1 == len(data):
                    print("{0}:{1}".format(chr(start), chr(data[index])))
                    break

                if data[index]+1 == data[index+1]:
                    index += 1
                elif data[index]+1 != data[index+1]:
                    print("{0}:{1}".format(chr(start), chr(data[index])), end="")
                    if index < len(data): print(", ", end="")
                    start = data[index+1]
                    index += 1           
                
    except:
        pass
        


