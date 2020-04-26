try:
    data = [4.00,4.50,5.00,2.00,1.50]
    x, y = [int(n) for n in input().split()]
    print("Total: R$ {:.2f}".format(data[x-1]*y))
except:
    pass