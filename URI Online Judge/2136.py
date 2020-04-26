if __name__ == "__main__":
    try:
        user, a = "", 0
        st_yes, st_no, data = [], [], {}
        while True:
            st = input().split()
            if len(st)==1 and st[0]=="FIM":
                break
            st_yes.append(st[0]) if st[1] == "YES" else st_no.append(st[0])
            if a == 0:
                a = len(st[0])
            elif a<len(st[0]) and st[1]=="YES":
                a = len(st[0])
                user = st[0]
        st_yes, st_no = list(set(st_yes)), list(set(st_no))
        st_yes, st_no = sorted(st_yes), sorted(st_no)
        st_yes.extend(st_no)
        for ch in st_yes:
            print(ch)
        
        print("")
        print("Amigo do Habay:")
        print(user)
    except:
        pass