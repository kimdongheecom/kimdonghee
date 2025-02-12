# ***********************
# -- 연산자
# ***********************
''' 
Python language supports the following types of operators −

Arithmetic Operators
Comparison (Relational) Operators
Assignment Operators
Logical Operators
Bitwise Operators
Membership Operators
Identity Operators
'''

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z) # returns True 
''' because z is the same object as x '''
print(x is y) # returns False 
''' because x is not the same object as y, even if they have thew same content '''
print(x == y) #  this comparison returns True
'''  
to demonstrate the difference betweeen "is" and "==":
because x is equal to y 
'''
12:26
# ***********************
# -- 비교문
# ***********************
# Single Statement Suites
var = 100
if ( var  == 100 ) : 
    print ("Value of expression is 100") # Value of expression is 100
print ("Good bye!") # Good bye!

# The else Statement
amount = int(input("Enter amount: "))

if amount<1000:
   discount = amount*0.05
   print ("Discount",discount)
else:
   discount = amount*0.10
   print ("Discount",discount)
    
print ("Net payable:",amount-discount)

#The elif Statement

amount = int(input("Enter amount: "))

if amount<1000:
   discount = amount*0.05
   print ("Discount",discount)
elif amount<5000:
   discount = amount*0.10
   print ("Discount",discount)
else:
   discount = amount*0.15
   print ("Discount",discount)
    
print ("Net payable:",amount-discount)