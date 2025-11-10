#Problem 1: Write down a Python program, using While loop that generates Odd no’s in between 1 
# to 100.
i=1
while i<=99:
    print(i,end=" ")
    i+=2

#Problem 2: Write down a Python Program using While loop to generate the following output.     
i=1
while i<=4:
    j=1
    while j<=14:
        print("*",end="")
        j+=1
    print()
    i+=1

i=1
while i<=8:
    j=1
    while j<=i:
        print("*",end="")
        j+=1
    print()
    i+=1    

i=1
while i<=7:
    j=7
    while j>=1:
        print("*",end="")
        j-=1
    print()
    i+=1                

#Problem 3:Write down a python program having one function for calculating factorial of a no.
#And call that function within a While loop to generate factorial of numbers from 0 to 10.

#Making a function:
def fact(x):
    if x==0 or x==1: #Assumption 0! and 1!
        final_result=1
    elif x>1 and x<11:
        facto=1
        for i in range(1,x+1):    
            facto=facto*i
            final_result=facto
    print(final_result)        

#Call that  function by using While loop:
x=0
while x<11:
    fact(x)  
    x+=1
 


