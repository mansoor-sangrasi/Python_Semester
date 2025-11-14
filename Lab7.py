# Problem 01:Construct the strings by using the string time format function strftime ()
#a) (Sunday, July 13 2025')
#b) ('09:40 PM Central Daylight Time on 07/13/2025')
#c) ('I will meet you on Thu July 13 at 09:40 PM.')

from datetime import datetime

#Create a date time object.
date_time=datetime(2025,7,13,21,40,)

#a) (Thursday, July 13 2025')

a=date_time.strftime("%A, %B %d %Y")
print(a)

#b) ('09:40 PM Central Daylight Time on 07/13/2025')

b=date_time.strftime('%I:%M PM Central Daylight Time on %m/%d/%Y')
print(b)

#c) ('I will meet you on Thu July 13 at 09:40 PM.')
c=date_time.strftime('I will meet you on %a %B %d at %I:%M PM.')
print(c)

#Problem 02:Assuming that variable forecast has been assigned string 'It will be a sunny day today' Write Python 
#statements corresponding to these assignments:

#(a) To variable count, the number of occurrences of string 'day' in string forecast. 
#(b) To variable weather, the index where substring 'sunny' starts.
#(c) To variable change, a copy of forecast in which every occurrence of substring 'sunny' is replaced by 'cloudy'.

forecast='It will be a sunny day today'

#(a) To variable count, the number of occurrences of string 'day' in string forecast.
count=forecast.count('day')
print(count)

#(b) To variable weather, the index where substring 'sunny' starts.
weather=forecast.index('sunny')
print(weather)

#(c) To variable change, a copy of forecast in which every occurrence of substring 'sunny' is replaced by 'cloudy'.
change=forecast.replace('sunny','cloudy')

print(change)     

#Problem 03:Write function even() that takes a positive integer n as input and prints on the screen all numbers between, and including, 2 and n divisible by 2 or by 3,
#using this output format:
#>>> even(17)
#2, 3, 4, 6, 8, 9, 10, 12, 14, 15, 16

#Making a function:
def even(x):
    for i in range(x):
        if i%2==0 or i%3==0:
            print(i,end=" ")                    
#Calling a function:
even(17)

#Problem 04:  Assume variables first, last, street, number, city, state, zipcode have already been assigned. Write a print statement that creates a mailing label:
#John Doe
#123 Main Street 
#AnyCity, AS 
#09876 
#assuming that:
#>>> first = 'John'
#>>> last = 'Doe'
#>>> street = 'Main Street'
#>>> number = 123
#>>> city = 'AnyCity'
#>>> state = 'AS'
#>>> zipcode = '09876'
first ="Mansoor"
last ="Ahmed"
street ="sangrasi street"
number ="77"
city ="Khipro"
state ="MS"
zipcode ="7374"
print(f"{first} {last}")
print(f"{number} {street}")
print(f"{city} {state}")
print(zipcode)

#Problem 05:Translate each part into a Python statement using appropriate string methods:

#(a) Assign to variable message the string 'The secret of this message is that it is secret.'
message="The secret of this message is that it is secret"
print(message)

#(b) Assign to variable length the length of string message, using operator len().
length=len(message)
print(length)

#(c) Assign to variable count the number of times the substring 'secret' appears in string message, using string method count().
count=message.count("secret")
print(count)

#(d) Assign to variable censored a copy of string message with every occurrence of substring
#'secret' replaced by 'xxxxxx', using string method replace().
censored=message.replace("secret","xxxxxx")
print(censored)

#Problem 06:  Write a function month() that takes a number between 1 and 12 as input and returns the
#three-character abbreviation of the corresponding month. Do this without using an if statement,
#just string operations. Hint: Use a string to store the abbreviations in order.
#>>> month(1)
#'Jan'
#>>> month(11)
#'Nov'

string="JanFebMarAprMayJunJulAugSepOctNovDec"
#Making a function:
def month(n):
    start_index=(n-1)*3
    end_index=start_index+3
    
    return string[start_index:end_index]
    

#Calling a function:
print(month(1))
print(month(2))
print(month(3))
print(month(4))   
print(month(5))
print(month(6))
print(month(7))
print(month(8))    
print(month(9))
print(month(10))
print(month(11))
print(month(12))   