#Program that will compute MPG (Miles covered Per Gallon used) for a car
#Where M is miles driven and G is gallon used


def calculateMpg(Miles, Gallon):
    MPG = (Miles / Gallon)
    return MPG





#Program that will compute the area of a circle
#Formula for area of circle is: A = Pi * r ** 2
#Let area of circle be A and r be radius
#Where Pi is 3.142 but we will be importing Pi in Python3

def calculateAreaOfCircle(radius):
    Area = math.pi * (radius ** 2)
    return Area






#program that will convert degrees celsius to degrees fahrenheit
#Formual for this conversion is TF = TC * (9 / 5) + 32
#Where TF is temperature in fahrenheit and TC is temperature in celsius

def convertFahrenheitToCelsius(TC):
    TF = TC * (9 / 5) + 32
    return TF







#DistanceBetweenPoints. The 2 points have coordinates (x,y) and (x1,y1)


def DistanceBetweenPoints(x,x1,y,y1):
    Distancehere = math.sqrt((x - x1)**2 - (y - y1)**2)
    return Distancehere

