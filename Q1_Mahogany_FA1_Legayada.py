import math

#Asks the user for the coordinates of sub one
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))

#Asks the user for the coordinates of sub two
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

#Calculates the distance of x and y
xd = float(math.pow(x2-x1, 2))
yd = float(math.pow(y2-y1, 2))

#Add the squared diiferences and find the square root
distance = float(math.sqrt(xd+yd))

#Round the answer to two decimal places
distance = round(distance, 2)

print("the distance between the two points is",distance,"")

"""
reflection:using math library is more practical because it provides ready madefunctions like sqrt() and pow() making the program shorter/easier to read and less prone to errors
"""