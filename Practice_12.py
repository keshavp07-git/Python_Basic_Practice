# Functions - It is a feature that allow us to re-use the code , suppose we write the code for Adding , we want to use with different numbers
# so , we write the code in that way so that we can use the code many times with different value.
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def add(arg1 , arg2):  # this is a function with return statement and that return statement stores in variable and we print
    total = arg1 + arg2
    return total

out = add(2,3)
print(out)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def adder(num1 , num2):  # This is a function without return statement but by default it return none if we use print statement then it will also print None
    sum = num1 + num2
    print(sum)

adder(10,20)  # it prints the sum only
print(adder(10,29)) # But it prints None because we are using print statement. it prints what's function returning that by default None.

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def sum(arg): # Pass the value in List or tuple format
    x=0
    for i in arg: # Pass all value to i from args
        x = x + i  # then now adding value from i into x and store into x
    return x # then return all value


sum1 = sum([1,2,3])# passed the all value in list in function "sum" and store in variable sum1
print(sum1) # print the variable

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def greet(msg="Sir"): # This is the Default Argument , Here we already declared default value for "msg" , argument that is Sir , if
    print(f"{msg},How are you?") # Don't give any argument then it don't throw any value
    print("Welcome to here !")

greet("Mr")



