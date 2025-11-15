# Problem 01:Write a program which will add your best five students name in a set. 
#You will use a loop to insert names in set.
five_students_name={'Majid','Mahaveer','Raja Parth','Tufail','Tofique'}
set=set()
for i in five_students_name:
    set.add(i)
print(set)

#Problem 02:Write a program which will remove 2 friends who left NED.

set_1={'Arslan','Siddique','Tufail','Tofique','Mansoor'}
set_1.discard('Arslan')
set_1.discard('Siddique')
print(set_1)

#Problem 03: Write a program which will add your best dishes and then pop one by one
#until the set is empty.
best_dishes=set()

#Add best dishes:

best_dishes.add("biryani")
best_dishes.add("Sindhri Pakora")
best_dishes.add('Pizza')
print(best_dishes)

#Pop one by one until the set is empty:
while best_dishes:
    empty_set=best_dishes.pop()
    print('Popped:',empty_set)
print('set will be empty.')    

#Problem 04: Write a program which will store number of items in a set 
#after each purchasing the items will be pop from the set and 
#compare its price at the end program will give you the total amount of items have been sold. 
# Also find the max amount and minimum amount of items sold

#items store in set_items with purchasing price.
set_items={('Mouse',500),('Keyboard',1200),('CPU',6000),('Laptop',10000)}

total_amount_of_items=0
sold_items=[500,1200,6000,10000]

while set_items:
    items_name,items_price=set_items.pop()
    total_amount_of_items+=items_price

print('Total amount of items',total_amount_of_items)
print('Maximum amount of items',max(sold_items))
print('Minimum amount of items',min(sold_items))

#Problem 05:  Write a program which will compare two sets, Set A and Set B.
#Both the sets have some students who love to play one is hockey and other one is cricket. 10 of them play both.
#Now using sets find how many of them are playing cricket only, if universal set is 40, students who play hockey are 21.

universal=40
only_hockey=21
only_circket=set()
both=10

# Formula = universal=only_hockey + only_cricket - both
only_circket=universal + both - only_hockey
print('The person who play only cricket is', only_circket)

#Problem 06:   A pet store keeps track of the purchases of customers over a four-hour period.
#  The store manager classifies purchases as containing a dog product, a cat product, a fish product, or product for a different kind of pet. She found.
#a.   83 purchased a dog product b.   101 purchased a cat product c.   22 purchased a fish product
#d.   31 purchased a dog and a cat product e.   8 purchased a dog and a fish product f.    10 purchased a cat and a fish product
#g.   6 purchased a dog, a cat and a fish product
#h.   34 purchased a product for a pet other than a dog, cat or a fish.
#i.   How many purchases were for a dog product only?
#ii.   How many purchases were for cat product only? iii.How many purchases for a dog or a fish product? iv.How many purchases were there in total?

D=83               #Total dog
C=101              #Total cat
F=22               #Total fish
other=34           
dog_and_cat=31
dog_and_fish=8
cat_and_fish=10
dog_and_fish_and_cat=6

#i)How many purchases were for a dog product only?

only_dog=D - dog_and_cat - dog_and_fish + dog_and_fish_and_cat
print('Only dog product is',only_dog)

#ii)How many purchases were for cat product only?

only_cat=C - dog_and_cat - cat_and_fish + dog_and_fish_and_cat
print('The only cat product is',only_cat)

#iii)How many purchases for a dog or a fish product?

dog_or_fish=D + F - dog_and_fish
print('The dog or fish product is',dog_or_fish)

#iv)How many purchases were there in total?

total=D + C + F - (dog_and_cat + dog_and_fish + cat_and_fish) + dog_and_fish_and_cat + other
print('The total purchases pet product is',total) 

#Problem 07:A camp of international students has 110 students, as shown in the diagram.
#The diagram will elaborate that all the students speak some kind of a language. 
#We need to find out how many that speak none of them out of 110 students.

#Data:
E=25         #only english
F=11         #only french
S=10         #only spanish
E_and_S=20
E_and_F=17
F_and_S=9
E_and_F_and_S=13
total_students=110
at_least_1_language=E + F + S + E_and_S + E_and_F + F_and_S + E_and_F_and_S

#We need to find out how many that speak none of them out of 110 students.

none_of_3_language=total_students - at_least_1_language
print('The students who speak none of three language',none_of_3_language)

#Find how many students speak.

students_speaks=total_students - none_of_3_language
print('the students who speak at least one language',students_speaks)

#a)English and Spanish but not French?

print('The students who speak English and Spanish is',E_and_S)

#b)Neither English, Spanish, nor French?

print('Students who not speak English,Spanish,French',none_of_3_language)

#c)French, but neither English nor Spanish?

print('Students who speak only french is',F)

#d)Only one of the three languages?

print('Total students who speak one language out of 3 is ',E + F + S)

#e)Exactly two of the three languages?

print('Total students who speak two language out of 3 is ',E_and_F + E_and_S + F_and_S)