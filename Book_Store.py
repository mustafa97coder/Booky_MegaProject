print(f"Bookstore Demo :")
print(f"===== Inputs & Output =====")

name = input("Enter your name : ")
age = int(input("Enter your age : "))
balance = int(input("Enter your wallet balance : "))
print(f" ")

print(f"Hello , {name}! welcome to Booky.")
print(f"Your age is {age} years old.\nEnjoy exploring our bookstore")
print(f" ")
list_book = []

print(f"===== BOOKSTORE MENU =====")
namebook1 = input("Enter the name of the first book : ")
list_book.append(namebook1)
price_book1 = int(input(f"Enter the price of {namebook1} Essentials : "))
print(f" ")

namebook2 = input("Enter the name of the Second book : ")
list_book.append(namebook2)
price_book2 = int(input(f"Enter the price of {namebook2} Essentials : "))
print(f" ")

namebook3 = input("Enter the name of the third book : ")
list_book.append(namebook3)
price_book3 = int(input(f"Enter the price of {namebook3} Essentials : "))
print(f" ")
print(f"Books added successfully Your book list : {list_book}")
Total_Price = price_book1 + price_book2 +price_book3
Average_Price = len(list_book) / Total_Price
print(" ")

print(f"===== NUMRIC FUNCTIONS =====")
print(f"...Calculating total price")
print(f"Total Price : {Total_Price}")
print(f"Rounded total : {round(Total_Price)}")
print(f"Average price per book : {Average_Price}")
print(f" ")

print(f"===== CONDITIONS CHECK =====")
if Total_Price >= 160 :
    print(f"Congratulations , {name}! You got a discount")
    discount = Total_Price * 0.1
    new_total = discount
    print(f"Your discounted total : {new_total}$ ")
else : 
    print(f"Sorry ,{name}! No discount this time.")
    print(f"Your total remains the same : ${Total_Price}")
print(f" ")

print(f"===== LIST OPERATIONS =====")
print(f"First book in your list : {list_book[0]}")
print(f"Last book in your list : {list_book[-1]}")
print(f"Sorted list : {list_book.sort()}")
print(f" ")

print(f"===== ARRAY OPERATION =====")
from array import array
import math
Array_Price = array("i",[price_book1 , price_book2 , price_book3])
print(f"Book prices array : {Array_Price}")
print(f"Sum of array : {sum(Array_Price)}")
Array_Max = max(Array_Price) 
Array_min = min(Array_Price)
print(f"Maximum price : {Array_Max}")
print(f"Minimum price : {Array_min}")
print(f" ")

print(f"===== SETS OPERATIONS =====")
Set_Category = {'Programming' , 'Technology' , 'Science'}
print(f"Available Category : {Set_Category}")
new_item_ = input("Enter a new category to add History : ")
new_item_Set = Set_Category.add(f'{new_item_}')
print(f"Updated categories : {Set_Category}")
print(f" ")

print(f"===== DICTIONARY OPERATIONS =====")
Dict_book_price = {
    namebook1:price_book1,
    namebook2:price_book2,
    namebook3:price_book3
}
print(f"Books and prices dictionary : {Dict_book_price}")
check_book = input("Enter a book name to check price : ")
if check_book == namebook1 :
    print(f"The price of {namebook1} is {price_book1}$")
elif check_book == namebook2 :
    print(f"The price of {namebook2} is {price_book2}$")
elif check_book == namebook3 :
    print(f"The price of {namebook3} is {price_book3}$")
print(f" ")

print(f"===== TUPLE OPERATIONS =====")
Tuple = ('Booky' , 'india')
print(f"Bookstore Info : {Tuple}")
print(f"Store name : {Tuple[0]}")
print(f"Country : {Tuple[1]}")
print(f" ")

print(f"===== WHILE LOOP SECTION =====")
while True :
    x = input(f"Do you want to see your book list again (yes/no) : ")
   
    if x == 'yes' :
        print(f"Your books : ")
        print(f"- {list_book[0]}") 
        print(f"- {list_book[1]}") 
        print(f"- {list_book[2]}")
        continue
    elif x == 'no' :
        break
print(" ")
import re 
word1 = r'^user'
word2 = r'name$'
pattern1 = re.match(word1 , name)
pattern2 = re.search(word2 , name)
if pattern1 and pattern2 :
    print(f'Valid username')
else :
    print("Invalid username")    
print(" ")

print(f"===== FUNCTION WITHOUT RETURN =====")
def summary() :
    print(f"Showing Summary : ")
    print(f"Customer : {name}")
    print(f"Total books : {len(list_book)}")
    print(f"Total price (after discount) : {Total_Price} ")
    print(f"Thanks you for shopping with Booky!")
summary ()
print(" ")

print(f"===== FUNCTION WITH RETURN =====")
def summary2 ():
    return f'Total returned from function : {Total_Price}'
fre = summary2
print(fre)
print(type(fre))
print(" ")

import sys 
print(f"===== SYS LIBRARY DEMO =====")
sys1 = sys.argv[1]
sys2 = sys.argv[2]
print(f"Program executed with system aguments : {sys1}")
print(f"All system arguments : {sys2}")
print(" ")

print(f"===== PROGRAM FINISHED =====")
print(" ")
print(f"Thank you {name.capitalize()} \nfor using Booky! Have a nice day ")









        

















