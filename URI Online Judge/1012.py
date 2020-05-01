def triangle_area(base, height):
    return .5*base*height

def circle_area(radious):
    PI = 3.14159
    return PI * (radious**2)

def trapezium_area(base1, base2, height):
    return ((base1+base2)/2) * height

def square_area(side):
    return side**2

def rectangle_area(side1, side2):
    return side1*side2

try:
    a,b,c = [float(x) for x in input().split()]
    print("TRIANGULO: {:.3f}".format(triangle_area(a,c)))
    print("CIRCULO: {:.3f}".format(circle_area(c)))
    print("TRAPEZIO: {:.3f}".format(trapezium_area(a,b,c)))
    print("QUADRADO: {:.3f}".format(square_area(b)))
    print("RETANGULO: {:.3f}".format(rectangle_area(a,b)))
except:
    pass