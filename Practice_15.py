# Variable length arguments **kwargs (keyword arguments) these two asterisk represents that we can use multiple arguments with keywords
# Or can say multiple keyword based argument.
# Multiple keyword based arguments store in dictionary in format of key and value whereas multiple arguments stores in tuples
''' Input : Multiple values for minutes , key=value pair activity
    Output : return sum of minutes + random minute spect on random activity
'''
import random
from random import choice


def time_activity(*args , **kwargs): # take multiple args and keyword based arges
    print(args) # print args tuple
    print(kwargs) # print kwargs in dictionary
    min = sum(args) + random.randint(0,60) # sum of args and add random int from 0 to 60
    print(min) # print the value
    choice=random.choice(list(kwargs.keys())) # Take random choice for key it returns tuple change into list now have random key and value.
    print(choice) # print only that key
    print(f"you have to spend {min} min for {kwargs[choice]}") # Now in printing format print {min} for minutes which is created and {kwargs[choice]}
    # choice have key and with help of kwargs we access the value and set into printing format. choice have key and kwargs value of it so
    # this return  {kwargs[choice]} value of key
time_activity(10,20,30, hobby="football" , sports="boxing" , fun="driving" , work="devops")