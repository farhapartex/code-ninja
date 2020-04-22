test = int(input())

for i in range(1,test+1):
    num, num_type = input().split()
    print("Case {0}:".format(i))
    if num_type == "bin":
        print("{0} dec".format(int(num,2)))
        print("{0} hex".format(hex(int(num,2))[2:]) )
    elif num_type == "dec":
        print("{0} hex".format(hex(int(num))[2:] ) )
        print("{0} bin".format( bin(int(num))[2:]))
    else:
        print("{0} dec".format(int(num, 16)))
        print("{0} bin".format(bin(int(num,16))[2:]))
    
    print("")

    