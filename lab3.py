# Problem 1:Write a program which solves the quadratic equation. The user will enter the value of a, b and c.
#The program will then check the denominator that if denominator is zero or not. If its zero it can
#reply the equation cannot solve as there is a zero division else, it will execute the program and will
#generate two solutions.

from math import sqrt
a=int(input("Enter value of a="))
b=int(input("Enter value of b="))
c=int(input("Enter value of c="))
x1=-b+sqrt(b**2-4*a*c)/2*a
x2=-b-sqrt(b**2-4*a*c)/2*a
if a==0:
   print("The equation cannot be solve because a==0")
else:
    print(round(x1),round(x2))

# Problem 2:Calculate the arithmetic sequence of n numbers. The program will generate the nth term of the
#sequence, whereas the user will enter the first term and the common difference. The program will
#then ask either to continue or not, if the user will enter yes it will ask the next nth term to calculate.
#Example: you have entered the first term as 3 and common difference 6 you are interesting in 35th
#term. So it will calculate and generate the answer as 207. Now it will again ask for you to continue
#if you agree it will ask next term like 45th or 96th term to calculate.
#  𝑎1 + (𝑛 − 1)𝑑

a1=int(input("Enter value of a1="))
d=int(input("Enter value of d="))
n=int(input("Enter nth term="))
tn=a1+(n-1)*d
print(tn)

#Problem 3: Write a program which will check either the giving string is Palindrome or not. Palindrome is a
#string when we reverse the string it will generate the original string. Example CIVIC, MOM, 010,
#1001, etc. So if you enter the word which is Palindrome it will say yes your string is Palindrome
#otherwise it will generate sorry message.
#[Hint: As user may enter upper or lower case, so you may use myString.casefold(). A casefold() will
#remove all the upper and lower case problems. To generate the reverse of string you can use reversed()
#function on your string.]

mystring=input("Enter string=")
mystring=mystring.casefold()
reversed_string="".join(reversed(mystring))

if mystring==reversed_string:
   print("Yes your string is palindrome")
else:
    print("Sorry your string is not palindrome")

#Problem 4:Write a program which will collect your name, your father’s name, your roll number and your
#subjects (5 Subjects with name and numbers). At the end it will generate a result with your name,
#your father’s name, your details subjects, marks you have obtained with total marks with grade and
#percentage.
#[Hint: Your creativity and analysis approach will be checked]

my_name=input("Enter your name:")
father_name=input("Enter your father name:")
roll_number=int(input("Enter your roll number:"))
result={}
for i in range(5):
    subject_name=input(f"Enter subject {i+1} name:")
    subject_mark=int(input(f"Enter mark of {subject_name}:"))
    result[subject_name]=subject_mark
total_mark=500
obtain_mark=sum(result.values())
percentage=(obtain_mark/total_mark)*100    
print(result)    
print(total_mark)
print(obtain_mark)
print(percentage)    
if percentage>=85 or percentage<=100:
    print("A")
elif percentage>70 or percentage<85:
    print("B")
else:
    print("C")

#Problem 5:Generate a table from initial value to final, depending upon the user starting and ending range in
#matrix form such as:
#1 2 3 4 5
#2 4 6 8 10
#3 6 9 12 15-
#4 8 12 16 20
#5 10 15 20 25

a=int(input("Taken user starting range:"))
b=int(input("Taken user ending range:"))
for i in range(a,b):
   print(1*i,end=" ")
print()
for j in range(a,b):
    print(2*j,end=" ")
print()
for x in range(a,b):
    print(3*x,end=" ")
print()
for y in range(a,b):
    print(4*y,end=" ")
print()
for z in range(a,b):
    print(5*z,end=" ")

#Problem 6:Write a program which will add two square matrices.

A=[
    [1, 2, 3],
    [2, 7, 8],
    [9, 7, 1]
]
B=[
    [5, 6, 10],
    [8, 2, 11],
    [9, 3, 12]
]
matrix_addition=[]
for i in range(3):
    matrix_addition.append([])


    for j in range(3):
        
        
        result=A[i][j]+B[i][j]
        matrix_addition[i].append(result)
for final_matrix_addition in matrix_addition:
    print(final_matrix_addition)

#Problem 07:Write a program which will multiply two square matrices.
A=[
    [1,2],
    [4,6]
]    
 

B=[
    [9,4],
    [8,7]
]

C=[
    [0,0],
    [0,0]
]

for i in range(2):
    for j in range(2):
        for k in range(2):
            C[i][j]+=A[i][k]*B[k][j]

for result_matrix in C:
    print(result_matrix)            



            
       
        
     





               






