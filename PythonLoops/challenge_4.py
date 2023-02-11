side1 = int(input('Enter 1st side of Triangle:'))
side2 = int(input('Enter 2nd side of Triangle:'))
side3 = int(input('Enter 3rd side of Triangle:'))

if side1 == side2 == side3:
    print("Equilateral Triangle")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")
