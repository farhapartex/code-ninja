try:
    n = int(input())
    print(n)
    print("{0} nota(s) de R$ 100,00".format(n//100))
    print("{0} nota(s) de R$ 50,00".format( (n%100)//50 ))
    print("{0} nota(s) de R$ 20,00".format( ((n%100)%50)//20 ))
    print("{0} nota(s) de R$ 10,00".format( (((n%100)%50)%20)//10 ))
    print("{0} nota(s) de R$ 5,00".format( ((((n%100)%50)%20)%10)//5 ))
    print("{0} nota(s) de R$ 2,00".format( (((((n%100)%50)%20)%10)%5)//2 ))
    print("{0} nota(s) de R$ 1,00".format( ((((((n%100)%50)%20)%10)%5)%2)//1 ))
except:
    pass