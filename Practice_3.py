# Strings
from typing import Tuple

print("-----------------------------------------------------------------------------------------------------------------------------------------------------")
str1 = "alpha"
str2 = 'beta'
str3 = """gamma"""
str4 = '''delta'''

#Numbers

num1 = 12
flt1 = 2.4


#List (It is a collection of multiple datatypes with ability of mutability) , A data structure in Python , use Square brackets
List = [str1 , "devops" , num1 , 2.4 , 45]
print(List)
print("------------------------------------------------------------------------------------------------------------------------------------------------------")
#Tuples (It is a collection of multiple datatypes with no ability to mutate them just immutable) , A data structure in Python , use round brackets
Tuples = (str1 , "devops" , num1 , 2.4 , 45)
print(Tuples)
print("-------------------------------------------------------------------------------------------------------------------------------------------------------")
#Dictionary (Elements in Dictionary are always in pairs),(key:value) Use curly braces
Dict = {"Name":"Keshav" , "Weight":75 , "Exercises":["Football", "Basketball"]}
print(Dict)
print("-------------------------------------------------------------------------------------------------------------------------------------------------------")
print("Type of DATA STRUCTURE",type(List))
print("Type of DATA STRUCTURE",type(Tuples))
print("Type of DATA STRUCTURE",type(Dict))

#Boolean
x = True
y = False
print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
print(x)
print(y)
print("-------------------------------------------------------------------------------------------------------------------------------------------------------")
print("Type of variable",type((x)))
print("Type of variable",type((y)))
