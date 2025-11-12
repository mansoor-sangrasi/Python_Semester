#Problem 1:Use  inbuilt min and max functions to perform
#the task of getting the minimum and maximum value of  in a list of tuples for a particular element
#position in a tuple.
Sample  = [(2, 3), (4, 7), (8, 11), (3, 6)]
print(max(Sample))
print(min(Sample))

#Problem 2:A dartboard of radius 10 and the wall it is hanging on are represented using the two dimensional 
# coordinate system, with the board’s center at coordinate (0; 0). Variables x and y store the x- and y-coordinate of a dart hit. 
# Write an expression using variables x and y that evaluates to True if the dart hits (is within) the dartboard, and
# evaluate the expression for these dart coordinates:
#(a) (0; 0)
#(b) (10; 10) (c) (6; 6)
#(d) (7; 8)
#x**2+y**2<=r**2 

#a) (0;0) Dart 1
x1=0
y1=0
print(x1**2+y1**2)
print(x1**2+y1**2<=100)

#(b) (10; 10) Dart 2
x2=10
y2=10
print(x2**2+y2**2)
print(x2**2+y2**2<=100)

#(c) (6; 6) Dart 3
x3=6
y3=6
print(x3**2+y3**2)
print(x3**2+y3**2<=100)

#(d) (7; 8) Dart 4
x4=7
y4=8
print(x4**2+y4**2)
print(x4**2+y4**2<=100)

#Problem 3:Write Python expressions corresponding to these statements:

#(a)The number of characters in the word "anachronistically" is 1 more than the number of characters in the word "counterintuitive."

print(len("anachronistically")==len("counterintuitive")+1)    

#(b)The word "misinterpretation" appears earlier in the dictionary than the word "misrepresentation."

print("misinterpretation"<"misrepresentation") 

#(c)The letter "e" does not appear in the word "ﬂoccinaucinihilipiliﬁcation".

A="ﬂoccinaucinihilipiliﬁcation"
if "e"in A:
    print("True")
else:
   print("False")

#(d)The number of characters in the word "counterrevolution" is equal to the sum of the number of characters in words "counter" and "resolution.

print(len("counterrevolution")==(len("counter")+len("revolution")))        

#Problem 4:Write a program in Python that holds an empty tuple and fill that tuple after taking user input for names of provinces of Pakistan 
#fill an empty tuple and print.

n1=input("Enter province first:")
n2=input("Enter second province:")
n3=input("Enter third province:")
n4=input("Enter fourth province:")
list=[]
list.append(n1)
list.append(n2)
list.append(n3)
list.append(n4)

#Convert list into tuple:

Tuple=tuple(list)
print(Tuple)


