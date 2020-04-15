if __name__ == "__main__":
    try:
        while True:
            n = int(input())
            if n == 0:
                break
            queue, res, last = [k for k in range(1,n+1)], [], 0
            
            print("Discarded cards: ", end="")
            if len(queue)==1:
                print("")
            while len(queue) > 1:
                print("{0}, ".format(queue[0]), end="") if len(queue) > 2 else print("{0}".format(queue[0]))
                del queue[0]
                d = queue[0]
                del queue[0]
                queue.append(d)
            
            print("Remaining card: {0}".format(queue[0]))
                
                
    except:
        pass