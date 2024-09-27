import math

x1 = float(input("Enter koordinate for x1: "))
y1 = float(input("Enter koordinate for y1: "))
x2 = float(input("Enter koordinate for x2: "))
y2 = float(input("Enter koordinate for y2: "))

print("distance between points:")
print(round(math.sqrt((x2-x1)**2+(y2-y1)**2)),2)