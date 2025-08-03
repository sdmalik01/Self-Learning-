# Basics syntax and things around python: such as variables, user inputs, loops, conditional statements, etc. 
# Variables:
number = 21
string = "Malik"
floatNumber = 26.58
lists = ["apple","banana","cherry"]
tuples = ("apple","banana","cherry")
distionary = {"key":"values","age":21}
sets = {"apple","banana","cherry"}
#To check the data type of the variable 
print(type(number)) #Output: <class 'int'>

#To assign multiple values:
x, y, z = 21, "malik", 25.89
'''Here x = 21, y = Malik, z = 25.89'''

# Data type casting: refers to changing the data type of the variable
x = 21
print(type(str(x)))

# python operators are used to perform functions and operations in the program.
# Arithmetic operatos: is used for arithmetic operations such as addition,substraction,multiplication,etc.
x = 6
y = 10
print(y-x) #Output: 4

#Assignment operator: assignment operator is used to assign values 
x = 7 
y += 8 # y=y+8
z %=10 # z = z%10 ---- % gives reminder of the result

# Comparison operators: use to compare values between two entities
a = 10
if x>=10:
    print("True") #Ouput: True

# logical operator: use for logical questions or multiple comparion 
p = 10
q = -20

if (p>0) and (q<0):
    print("True")
#Output: True

'''Bitwise operator for binary questions, membership operator for checking if sequence is presented in object or not etc'''

#Python Data Types: 

#Lists:
mylist = ["apple","banana","cherry"]
'''1.List item are ordered, changeable, and allow duplicate values
   2.List items are indexed, the first item has index [0]
   3.List can store multiple data types
'''
exlist = ["apple",21,"Malik",52.04,"Something"]

print(exlist[0]) #print: "apple"
exlist[0] = "banana" #replace apple with banana

'''Adding methods in list'''
exlist.append("Ayesha") # add Ayesha at the end of the list
exlist.insert(1,"orange") #inserting element at fixed position
exlist.extend(mylist) # Make one single list from two list basically by excenting first one with the second one.
myset = ("IICT","JNEC")
exlist.extend(myset) # Extent works with other iterables also such as sets,tuples,dictionaries,etc

'''Remove methods in list'''

exlist.remove("banana") #removes banana from list - Always removes the first occurence of item in the list
exlist.pop(1) # removing item with its index
exlist.pop() #removes the last item in the list
del exlist[0] # also removes with list index
exlist.clear() #Clears the whole list

'''Sorting of list'''

