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

exlist.sort() # alphabatically sorted 

thislist = [23,56,14,12,58,90]
thislist.sort() #Sorted in ascending order
thislist.sort(reverse=True) #Sorted in descending order

#customized sorting function:
def myfunc(n):
    return abs(n - 50)

funclist = [100,25,26,12,58,90]
funclist.sort(key = myfunc)  # customized sorting according to the function

#Copying list:

secondlist = exlist.copy() #second list contains same as exlist list now
secondlist = list(exlist)
secondlist = exlist[:]

# Joining list:

list1 = ["a","b","c"]
list2 = [1,2,3]

list3 = list1 + list2 #list3 = ["a","b","c",1,2,3]
for x in list2:
    list1.append(x)
list1.extend(list2)

'''Tupple: Tuple items are ordered, indexed, unchangable, and allow duplicate values // Many methods are same in array data structures such as list,tuple,etc'''
thistuple = ("apple","banana","cherry","mango")

print(len(thistuple)) #Gives the length of the data structure: such as tupple,list etc.

newtuple = ("apple",1,"cherry",2) #tuple can contain diffrent data structures

#unpacking in tuple:
fruits = ("apple","mango","cherry","banana","watermelon")
(green,yellow,*red) = fruits
print(green) #apple
print(yellow) #mango
print(red) #["cherry","banana","watermelon"] : with * all the rest values are assign to red only

#Sets: Set items are unordered, unchangeable and do not allow duplicate value.
exset = {"abc",1,"ipl",12,"malik"} # set can have different data types.

for x in exset:
    print(x) #prints elements of set
print("banana" in exset) #True if banana is in exset else false
print("apple" not in exset) #True if apple is not in exset else false

'''Once tuple is created u cannot change the items but u can new items '''
exset.add("orange") #add orange in the starting of set

ex2set = ("juice","pani-puri","samosa","chaat")
exset.update(ex2set) #Make single set from both the sets
'''Through update u can add any iterable such as list etc'''

exset.remove(1) #removes 1 from the set
exset.discard(1) #same as remove but not will raise an error if the discarding element is not present in the set.

exset.pop() #removes a random element from set
exset.clear() #clear out the set
del exset #will delete the set completely

#Join Sets:

set1 = {1,2,3}
set2 = {"a","b","c"}

'''UNION'''
set3 = set1.union(set2) # set3 contains elements from both the sets UNION!
set3 = set1 | set2 #Same as union
set3 = set1.union(set2,exset,ex2set) #can join many sets
set3 = set1 | set2 | exset | ex2set #same as above
'''U can union diffrent data types too but only with union() not | operator'''
set1.update(set2) #random adding of both sets

'''INTERSECTION'''
set3 = set1.intersection(set2) #Set3 contains elements present in both the sets
set3 = set1 & set2 #same as intersection
set1.intersection_update(set2) #keep only duplicates, but it will change the original set instead of making a new set

'''DIFFERENCE'''
set3 = set1.difference #will return a new set that will contain only the items from the set that are not present in the other set.
set3 = set1 - set2 #same as above
set1.difference_update(set2) #Keep the items that are not prsent in both sets.
set3 = set1.symmetric_difference(set2) #Keep only the elements that are NOT present in both sets.

'''
Dictionary: 
1.Dictionary are written with curly brackets, and have keys and values.
2.Dictionary items are ordered, changeable, and do not allow duplicates.
dictionary items are presented in key:value pairs, and can be referred to using the key name.
'''
thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "year": 1964
}
x = thisdict['model'] #Output: Mustang
x = thisdict.get("model") #Output: Mustang

y = thisdict.keys() #This method will give list of the keys in the dictionary.
thisdict["new_model"] = "Mustang GT" #Add item to dictionary.

z = thisdict.values() #this method will give list of values.

l = thisdict.items() #this method will give (key,value) pairs in tuple.

#Checking if key exists in dictionary or not:
if "model" in thisdict:
    print("Yes model is there in key") #Standard the loop will go through keys.

thisdict["brand"] = "BMW" #Change the value of brand key.
thisdict.update({"year": 2020}) #update/change the value of key.

thisdict.pop("model") #Remove pop key value pair.
del thisdict["model"] #Same as above.
thisdict.popitem() #removes random key value pair.
thisdict.clear() #clear the dictionary.

for x in thisdict:
    print(x)   #Prints keys in dictionary.
for x in thisdict.keys():
    print(x) #prints keys as looping through keys.
for y in thisdict:
    print(thisdict[y]) #prints values in dictionary.
for y in thisdict.values():
    print(y) #Gives values as looping through values.
for x,y in thisdict.items():
    print(x,y) #loop thorugh every item in dictionary.

mydict = thisdict.copy() #Copy the whole dictionary into a new dictionary.
mydict = dict(thisdict) #same as above.

#Nested dictionary:

myfamily = {
    "child1":{
        "name":"emil",
        "year":2004
    },
    "child2":{
        "name":"malik",
        "year":2005
    },
    "child3":{
        "name":"Ayesha",
        "year":2006
    }
}

'''OR'''

child1 = {
    "name":"emil",
    "year":2004
}
child2 = {
    "name":"Malik",
    "year":2005
}
child3 = {
    "name":"Ayesha",
    "year":2006
}

myfamily = {
    "child1":child1,
    "child2":child2,
    "child3":child3
}

print(myfamily["child2"]["name"])  #Acessing nested items.


'''Conditional statements'''
a = 33
b = 55
if a==b:
    print("a=b")  #condition checking using if-elif-else statements:
elif a!=b:
    print("a is not equal to b")
else:
    print("Nothing!")

'''Python Match'''
day = 4
match day:
    case 1:
        print("Mon")
    case 2:
        print("Tue")
    case 3:
        print("wed")
    case 4:
        print("thur")
    case 5:
        print("Fri")
    case 6:
        print("Sat")
    case 7:
        print("Sun")
    case _: #Default case
        print("This is defualt return")

#Or statement----
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("---Normal Day---")
    case 6 | 7:
        print("---Weekend---")
#if statement Guards:
month = 4
match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("Normal day in April")
    case 6 | 7 if month == 5:
        print("This weekend in may!")
    case _:
        print("No match!")

#Loops in python: While,For ---
i = 1
while i < 6: #Loop until the condition is true. use when we dont know the ending condition.
    print(i)
    i+=1
    if i==5:
        break   #Break statement stops at the condition when true.
while i < 10:
    print(i)
    if i==5:
        continue    #Continue statement skips the continue code and start from first like continue.
    i+=1

'''For loop:'''
for x in range(2,6,2): #Loop from 2-6 (But not including 6) -- with 2 steps increament.
    print(x)

color = ["red","yellow","green","blue","black"]
fruits = ["apple","mango","guava","berry","avacado"]

for x in color:
    for y in fruits:
        print(x,y)

for x in range(1,3):
    pass            #pass is written where u want nothing execution through this it will not get an error

'''-----Functions-----'''
def function_name():
    print("Hello World") #Statement

function_name() #function call

def try_fun(fname):
    print(fname + "Reference")

try_fun("Malik")    #Parameters and arguments can refer same thing: values passed in the function.
try_fun("Ayesha")   
try_fun("Muktar")

def fun1(name,age,course):      #parameters can be more then one in functions
    print("My name is: ", name,"I am ",age,"old","i am persuing", course)
#if parameters are 3 and u pass only 2 it will give an error hence for this u will nedd defualt arguments in functions.
def fun2(name,age,course="btech"):
    print("Course: " + course)  #if nothing is passed in function call for course the defualt value will be taken.


