if __name__ == "__main__":
    try:
        while True:
            st = input()
            if st[0] == "*":
                break
            data = [word[0].upper() for word in st.split()]
            print("Y") if len([ True for let in data if let == data[0] ]) == len(data) else print("N")
    except:
        pass