try:
    n = float(input())
    if n < 0.0 or n > 100.0:
        print("Fora de intervalo")
    elif n <=25.0 and n >= 0.0:
        print("Intervalo [0,25]")
    elif n > 25.0 and n <= 50.0:
        print("Intervalo (25,50]")
    elif n > 50.0 and n <= 75.0:
        print("Intervalo (50,75]")
    elif n > 75.0 and n <= 100.0:
        print("Intervalo (75,100]")
except:
    pass