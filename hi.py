import math
def area_rectangle(l,b):
    return l*b
def area_square (s):
    return s*s
def area_circle(r):
    return math.pi *r*r
def area_triangle (b,h):
    return 0.5*b*h
l=float(input("Enter the length of rectangle:"))
b=float(input("Enter the breadth of rectanle:"))
print("area of rectangle =",area_rectangle(l,b))
s=float(input("\nEenter side of square:"))
print ("area of square=",area_square(s))
r=float(input("\nEnter radius of circle:"))
print("area of circle=",area_circle(r))
base=float(input("\nEnter base of triangle:"))
h=float(input("Enter height of triangle:"))
print("area of triangle =",area_triangle(b,h))
