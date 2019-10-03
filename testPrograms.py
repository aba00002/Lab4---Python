from aba00002Library import calculateMpg 
m = float(input("enter the number of miles driven"))
g = float(input("enter the number of gallons used"))
mpg = calculateMpg(m, g)
print("Dear driver, the mile per gallon rate of your car is", mpg)



from aba00002Library import calculateAreaOfCircle
import math
r = float(input("Enter the radius of the circle"))
A = calculateAreaOfCircle(r)
print("Dear user, the Area of your circle is", A )



from aba00002Library import convertFahrenheitToCelsius
TC = float(input("What is the temperature in celsius?"))
F = convertFahrenheitToCelsius(TC)
print("Dear user, The temperature in fahrenheit equivalent of your entry is", F)



from aba00002Library import DistanceBetweenPoints
import math
x = int(input("What is the cordinate of x?"))
x1 = int(input("What is the cordinate of x1?"))
y = int(input("What is the cordinate of y?"))
y1 = int(input("What is the cordinate of y1?"))
D = DistanceBetweenPoints(x,x1,y,y1)
print("The distance between the two points is", D)
