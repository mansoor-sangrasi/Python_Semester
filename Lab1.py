#Problem 1:Write a program for converting Centigrade to fahrenhiet degree.

Centigrade=int(input("Enter centigrade temperature ="))
fahrenhiet=(9/5*Centigrade)+32
print("Temperature in fahrenhiet is",fahrenhiet)

#Problem 2:   Write a program for converting Degree
#Fahrenhiet to Centigrade.

Fahrenhiet=int(input("Enter fahrenhiet temperature="))
Centigrade=(Fahrenhiet-32)*5/9
print("Temperature in Centigrade is",Centigrade)

#Problem 3:Write a program to calculate area of rectangle.

length=int(input("Enter length of rectangle="))
width=int(input("Enter width of rectangle="))
area_of_rectangle=length*width
print("Area of rectangle is",area_of_rectangle)

#Problem 4:Write a program to calculate the volume of sphere.

import math
r=int(input("Enter radius of Volume="))
V=4/3*(math.pi)*r**3
print("Volume of sphere is",V)

#Problem 5:Write your name in uppercase,lowercase,titlecase.

name="Mansoor Ahmed"
print(name.upper())
print(name.lower())
print(name.title())

#Problem 6:Calculate Compound Interest by taking user input.

P=int(input("Enter Principal Amount="))
R=int(input("Enter Rate="))
T=int(input("Enter Time Span="))
A=P*(1+R/100)*T
Compound_interest=A-P
print("Compound interest is",Compound_interest)


