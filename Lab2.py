#Problem 1:A ball at the end of a string is revolving uniformly in a horizontal circle of radius 2 meters at
#constant angular speed 10 rad/s. Determine the magnitude of the linear velocity of a point located:
#(a) 0.5 meters from the center
#(b) 1 meter from the center
#(c) 2 meters from the center
#Known: Radius (r) = 0.5 meters, 1 meter, 3 meters, The angular speed = 10 radians/second
#Wanted: The linear velocity

w=10
r1=0.5
r2=1
r3=3
V1=r1*w
V2=r2*w
V3=r3*w
print(V1)
print(V2)
print(V3)

#Problem 2:The blades in a blender rotate at a rate of 5000 rpm. Determine the magnitude of the linear
#velocity:
#(a) a point located 5 cm from the center
#(b) a point located 10 cm from the center
#Known: Radius (r) = 5 cm and 10 cm
#The angular speed (ω) = 5000 revolutions / 60 seconds = 83.3 revolutions / second = (83.3)(6.28 radian) /
#second = 523.3 radians / second
#Wanted: The magnitude of the linear velocity

w=523.3
r1=0.05
r2=0.1
V1=r1*w
V2=r2*w
print(V1)
print(V2)

#Problem 3:A point on the edge of a wheel 30 cm in radius, around a circle at constant speed 10
#meters/second.
#What is the magnitude of the angular velocity?
#Known: Radius (r) = 30 cm = 0.3 meters, The linear velocity (v) = 10 meters/second
#Wanted: the angular velocity

V=10
r=0.3
w=V/r
print("The angular velocity is",w)

#Problem 4:. A car with tires 50 cm in diameter travels 10 meters in 1 second. What is the angular speed?
#Known:
#Radius (r) = 0.25 meter, The linear speed of a point on the edge of tires (v) = 10 meters/second
#Wanted: The angular speed

V=10
r=0.25
w=V/r
print("The angular velocity is",w)

#Problem 5:The angular speed of wheel 20 cm in radians is 120 rpm. What is the distance if the car
#travels in 10 seconds.
#Known: Radius (r) = 20 cm = 0.2 meters
#The angular speed = 120 rev / 60 seconds = 2 rev / second = (2)(6.28) radians / second = 12.56 radians /
#second
#Wanted: distance
w=12.56
r=0.2
t=10
V=r*w
d=V*t
print("distance will be",d)

#Problem 6: A car is running at a velocity of 50 miles per hour and the driver accelerates the car by 10
#miles/hr2. How far the car travels from this point in the next 2 hours, if the acceleration is
#constant. Formula: v = u + at

a=10
u=50
t=2
v=u+a*t
print("Velocity in next 2 hour is",v)

#Problem 7: A Stone is dropped freely from a height of 100 feet. With what velocity will it hit the ground?
#(Neglect the air resistance and assume the acceleration due to gravity is 32ft/s2).
#Formula: 2gh=v**2-u**2

import math
u=0
h=100
g=32
v=2*g*h
print("When Stone hit the ground its Velocity will be",math.sqrt(v))



        




