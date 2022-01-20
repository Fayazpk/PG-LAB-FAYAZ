from graphics import rectangle
from graphics import circle
from graphics import sphere
from graphics import cuboid

print("Read values: \n Rectangle:\n")
l=int(input("Enter length"))
b=int(input("Enter breadth"))
r_area=rectangle.area(l,b)
r_perimeter=rectangle.perimeter(l,b)


r=int(input("enter the radius of circle"))
print(circle)
circle.area(r)
circle.perimeter(r)


l=int(input("Enter the length of Cuboid: "))
b=int(input("Enter the breadth of Cuboid: "))
h=int(input("Enter the height of Cuboid: "))
cuboid.area(l,b,h)
cuboid.perimeter(l,b,h)
print()
r=int(input("Enter the radius of Sphere: "))
sphere.area(r)
sphere.volume(r)
