# Problem 1 Take a sample list [2, 1, 3, 5, 4, 3, 8]
#Apply del(), remove(), sort(), insert(), pop(), extend() 

#Apply remove():
list=[2,1,3,5,4,3,8]
list.remove(2) 
print(list)

#Apply pop():
list1=[2,1,3,10,11,13]
list1.pop(0)
print(list1)

#Apply del() it's not a method it is keyword del
list2=[1,2,3,4,5,6]
del list2[3]
print(list2)

#Apply insert():
list2.insert(0,"Mansoor")
print(list2)
#Apply extend():
list2.extend([30,5])
print(list2)

#Apply sort():
l1=[40,36,10,3,2,11]
l1.sort()  #Ascending Order
print(l1)
l1.sort(reverse=True) #Descending order
print(l1)

#Problem 2:  A ladder put up right against a wall will fall over unless put up at a certain angle less than
#90 degrees. Given variables length and angle storing the length of the ladder and the  angle that  it  forms  with  the  ground  as  it  leans  against  the  wall,  write  a  Python  expression involving length and angle that computes the height reached by the ladder. Evaluate the expression for these values of length and angle:
#(a)16 feet and 75 degrees (b)20 feet and 0 degrees (c)24 feet and 45 degrees (d)24 feet and 80 degrees
#Note: You will need to use the trig formula:
#height = length * sin(angle)
#The math module sin() function takes its input in radians. You will thus need to convert the angle given in degrees to the angle given in radians using:
#radians = π * degrees / 180

#a)16 feet and 75 degrees.
import math
l1=16
d1=75
r1=math.pi*d1/180
h1=l1*math.sin(r1)
print(round(h1))

#b)20 feet and 0 degrees.
l2=20
d2=0
r2=math.pi*d2/180
h2=l2*math.sin(r2)
print(h2)
print(round(h2))

#c)24 feet and 45 degrees.
l3=24
d3=45
r3=math.pi*d3/180
h3=l3*math.sin(r3)
print(h3)
print(round(h3))

#d)24 feet and 80 degrees.
l4=24
d4=80
r4=math.pi*d4/180
h4=l4*math.sin(r4)
print(h4)
print(round(h4))

# Problem 3:Write the relevant Python expression or statement, involving a list of numbers lst and using
#list operators and methods for these speciﬁcations:
#(a)An expression that evaluates to the index of the middle element of list
#(b)An expression that evaluates to the middle element of list
#(c)A statement that sorts the list  in descending order
#(d)A statement that removes the ﬁrst number of list  and puts it at the end
#Note: If a list has even length, then the middle element is deﬁned to be the rightmost of
#the two elements in the middle of the list.

#(a)An expression that evaluates to the index of the middle element of lst
#(b)An expression that evaluates to the middle element of lst
   #Note: If a list has even length, then the middle element is deﬁned to be the rightmost of
#the two elements in the middle of the list.

list=[10,20,30,40,50,60] #When length of list is even.
middle_index=len(list)//2
middle_element=list[middle_index]
print(middle_index)
print(middle_element)

#(c)A statement that sorts the list  in descending order.

list1=[2,10,7,5,9,8]
list1.sort(reverse=True)
print(list1)

#(d)A statement that removes the ﬁrst number of list  and puts it at the end.

ist2=[23,24,25,26]
remove_variable=list2.pop(0)
list2.append(remove_variable)
print(list2)

# Problem 4:Start by assigning to variables monthsL and monthsT a list and a tuple, respectively, both containing strings 'Jan', 'Feb', 'Mar', and 'May', in that order. Then attempt the following with both containers:
#(a)Insert string 'Apr' between 'Mar' and 'May'.
# (b)Append string 'Jun'.
#(c)Pop the container.
#(d)Remove the second item in the container. (e)Reverse the order of items in the container.

monthsL=['Jan','Feb','Mar','May']
monthsT=list(('Jan','Feb','Mar','May')) #Convert Tuple into List to Apply the following condition As direct we don't apply in Tuple this conditon b/c Tuple is immutable

#(a)Insert string 'Apr' between 'Mar' and 'May'.

monthsL.insert(3,'Apr')
monthsT.insert(3,'Apr')
print(monthsL)
print(monthsT)

# (b)Append string 'Jun'.

monthsL.append('Jun')
monthsT.append('Jun') 
print(monthsL)
print(monthsT)

#(c)Pop the container.

monthsL.pop()
monthsT.pop() 
print(monthsL)
print(monthsT)

#(d)Remove the second item in the container.

monthsL.remove('Feb')
monthsT.remove('Feb') 
print(monthsL)
print(monthsT)
      
#(e)Reverse the order of items in the container.
print(monthsL[::-1])
print(monthsT[::-1])

#Problem 5:Write the corresponding Python assignment statements: (a)Assign 6 to variable a and 7 to variable b.
#(b)Assign to variable c the average of variables a and b.
#(c)Assign to variable inventory the list containing strings 'paper', 'staples', and 'pencils'.
#(d)Assign to variables first, middle and last the strings 'John', 'Fitzgerald', and 'Kennedy'. 
#(e)Assign to variable fullname the concatenation of string variables first, middle, and last. Make sure you incorporate blank spaces appropriately.

#(a)Assign 6 to variable a and 7 to variable b
a=6
b=7

#(b)Assign to variable c the average of variables a and b.
c=(a+b)//2
print(c)
#(c)Assign to variable inventory the list containing strings 'paper', 'staples', and 'pencils'

inventory = ['paper', 'staples', 'pencils']

#(d)Assign to variables first, middle and last the strings 'John', 'Fitzgerald', and 'Kennedy'.
first="John "
middle="Fitzgerald "
last="Kennedy "
#(e)Assign to variable fullname the concatenation of string variables first, middle, and last. Make sure you incorporate blank spaces appropriately.
fullname=first+middle+last
print(fullname)