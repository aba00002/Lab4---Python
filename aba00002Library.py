#Program that will compute MPG (Miles covered Per Gallon used) for a car
#Where M is miles driven and G is gallon used


def caculateMpg(Miles, Gallon):
    MPG = (Miles / Gallon)
    return MPG

Miles = float(input("enter the number of miles driven"))
Gallon = float(input("enter the number of gallons used"))
print("Dear driver, the mile per gallon rate of your car is", caculateMpg(Miles, Gallon))




#Program that will compute the area of a circle
#Formula for area of circle is: A = Pi * r ** 2
#Let area of circle be A and r be radius
#Where Pi is 3.142 but we will be importing Pi in Python3

def calculateAreaOfCircle(radius):
    Area = math.pi * (radius ** 2)
    return Area

import math
radius = float(input("Enter the radius of the circle"))
print("Dear user, the radius of your circle is", calculateAreaOfCircle(radius))





#program that will convert degrees celsius to degrees fahrenheit
#Formual for this conversion is TF = TC * (9 / 5) + 32
#Where TF is temperature in fahrenheit and TC is temperature in celsius

def convertFahrenheitToCelsius(TC):
    TF = TC * (9 / 5) + 32
    return TF

TC = float(input("What is the temperature in celsius?"))
print("Dear user, The temperature in fahrenheit equivalent of your entry is", convertFahrenheitToCelsius(TC))





#DistanceBetweenPoints. The 2 points have coordinates (x,y) and (x1,y1)


def DistanceBetweenPoints(x,x1,y,y1):
    Distancehere = math.sqrt((x - x1)**2 - (y - y1)**2)
    return Distancehere

import math
x = int(input("What is the cordinate of x?"))
x1 = int(input("What is the cordinate of x1?"))
y = int(input("What is the cordinate of y?"))
y1 = int(input("What is the cordinate of y1?"))
print("The distance between the two points is", DistanceBetweenPoints(x,x1,y,y1))