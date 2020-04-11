if __name__ == "__main__":

    try:
        while True:
            st = input().split()
            initial, get_value, cnt = False, False, 0
            for index in range(0, len(st)):
                if not initial:
                    prev = st[index][0].lower()
                    initial = True
                else:
                    if prev == st[index][0].lower():
                        if get_value:
                            continue
                        else:
                            cnt += 1
                            get_value = True
                    else:
                        prev = st[index][0].lower()
                        get_value = False 
            
            print(cnt)
    except:
        pass

        