from decimal import Decimal
try:
    a = float(input())
    b = float(input())
    avg = (a*3.5) + (b*7.5)
    print("MEDIA = {:.5f}".format(avg/11))
except:
    pass