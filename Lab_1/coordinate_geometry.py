import math

x1 = int(input("Enter x1 "))
y1 = int(input("Enter y1 "))
x2 = int(input("Enter x2 "))
y2 = int(input("Enter y2 "))

first = (x2-x1)**2
#print(first)

second = (y2-y1)**2
#print(second)

result = math.sqrt((first+second))
print("Distance is: " , result)