if __name__ == "__main__":
    try:
        while True:
            trace = input()
            procs = int(input())
            cnt, cycles = 0, 0
            for i in range(0, len(trace)):
                if trace[i] == 'R':
                    cnt += 1
                    if i == len(trace)-1:
                        if cnt > 0:
                            res, div = cnt//procs, cnt%procs
                        cnt=0
                        cycles += res
                        if div>0: cycles += 1
                elif trace[i]=='W':
                    cycles += 1
                    if cnt > 0:
                        res, div = cnt//procs, cnt%procs
                        cnt=0
                        cycles += res
                        if div>0: cycles += 1
            
            print(cycles)
    except:
        pass