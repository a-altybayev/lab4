#task 1
import math
a = int(input("Input degree: "))
print("Output radian: ", math.radians(a))

#task 2
def trapezoid():
    h=int(input('Height:'))
    a=int(input('Base, first value: '))
    b=int(input('Base, second value: '))
    print(h*(a+b)/2)
trapezoid()

#task 3
import math
def polygon_area():
    n=int(input("Input number of sides: "))
    l=int(input("Input the lenght of a side: "))
    a=(n*pow(l,2))/4*math.tan(math.pi/n)
    print('The area of the polygon is', math.ceil(a))
polygon_area()

#task 4
def parallelogram():
    a = int(input('Lenght of base:'))
    h = int(input("Height of parallelogram:"))
    print("Expected Output:",float(a*h))
parallelogram()