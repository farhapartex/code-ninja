if __name__ == "__main__":
    try:
        test_case = int(input())

        for i in range(test_case):
            n,k,p = input().split()
            n,k,p = int(n), int(k), int(p)
            d = p%n
            ans = k+d
            ans = ans-n if ans>n else ans
            print("Case {0}: {1}".format(i+1,ans))
    except:
        pass

"""
*** Test cases ***

10
21 14 68
Case 1: 19
14 3 170
Case 2: 5
18 17 159
Case 3: 14
2 2 106
Case 4: 2
7 1 28
Case 5: 1
9 9 196
Case 6: 7
11 9 37
Case 7: 2
11 8 37
Case 8: 1
"""