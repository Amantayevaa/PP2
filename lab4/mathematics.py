
#1
import math
degree = float(input("Input degree:" ))
print("Output radian: ", math.radians(degree))

#2
Height = int(input("Height: "))
a = int(input("Base, first value: "))
b = int(input("Base, second value: "))
S = (a + b)*Height/2
print(f"Expected Output: {S}")

#3
import math
n = int(input("Input number of sides: "))
l = int(input("Input the length of a side: "))
Area = int(((l**2) * n)/(4 * math.tan(math.pi/n)))
print(f"The area of the polygon is: {Area}")

#4
l = int(input("Length of base: "))
h = int(input("Height of parallelogram: "))
S = float(l * h)
print(f"Expected Output: {S}")
