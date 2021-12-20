def fun (p):
    '''Panduan untuk function'''
    print(p)

fun('ini yang di print')

def FunctionName (p,l):
    "Function to multiply between 2 variable (int/float,int/float) return as number"
    return p*l

temp=FunctionName(2,2)
print(f"{temp}")

# Function definition is here
def printinfo( name, age = 26 ):
 "This prints a passed info into this function"
 print("Name: ", name)
 print("Age: ", age)
 return;

# Now you can call printinfo function
printinfo( age=50, name="hacktiv8" )
printinfo( name="hacktiv" )

# Varible Length 
def my_min(*args):
    result=99
    for num in args:
        if num < result:
            result = num
    return result

print("\nMin value = ",my_min(4, 5, 6, 7, 2))

#Lambda the anonym function
coba=lambda num1,num2:num1+num2

print(coba(1,2))

#function return 2 value
def sum( arg1, arg2 ):
    total = arg1 + arg2 # Here total is local variable.
    print("Inside the function local total : ", total)
    return total,arg1+10        

print("function dengan 2 value = ",sum(2,2))

#import from module / file py lain
import Person 

print("\nName = ",Person.name)
Person.display("Display Function Person")

#import from module / file py lain (beda folder)
import module.Person2 as p

print("\nName = ",p.name)
p.display("Display Function Person2")

#import from module / file py lain (objek saja)
from Person import name as p_name,display as p_display 

p_display(f"\n\nimport object dari module lain\nDisplay Function Person {p_name}")

from Sesi2.sesi2 import sesi2 as pkg
print("\nImport dari package/ folder luar lain\n total_purchase_sesi2 = ",pkg)