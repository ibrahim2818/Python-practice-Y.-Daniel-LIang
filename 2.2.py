# (Compute the volume of a cylinder) Write a program that reads in the radius and
#  length of a cylinder and computes the area and volume using the following formulas:
#  area = radius * radius * π
#  volume = area * length
import math
A,B= map(float, input ("enter the radius and length of the cylinder: ").split(","))

area = A * A * math.pi
volume = area * B
print(f"the area of the cylinder is {area:.4f}")
print(f"the volume of the cylinder is {volume:.4f}")
