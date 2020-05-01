try:
    n = int(input())
    print("{0} ano(s)".format(n//365))
    print("{0} mes(es)".format( (n%365)//30 ))
    print("{0} dia(s)".format( (n%365)%30 ))
except:
    pass