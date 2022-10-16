from calendar import c


a=float(input("Enter first side of triangle"))
b=float(input("Enter second side of the triangle"))
c=float(input("Enter third side of the triangle"))
s=(a+b+c)/2
area=(s*(s-a)(s-b)(s-c))**0.5
print("area of a triangle is:",area)
