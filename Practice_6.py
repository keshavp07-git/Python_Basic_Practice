print("-----------------------------------------------------------------------------")
print("------------------------Arithmatic Operator---------------------")
x = 2
y = 6

total = x+y
print(total)

total = x-y
print(total)

total = x*y
print(total)

total = x**y
print(total)

total = x/y
print(total)

total = x%y
print(total)

print("-----------------------------------------------------------------------------")
print("----------------comparison Operator---------------------------")

a = 30
b = 60

out = (a < b)
print(out)

out = (a > b)
print(out)

out = (a == b)
print(out)

out = (a != b)
print(out)

out = (a <= b)
print(out)

out = (a >= b)
print(out)

print("-----------------------------------------------------------------------------")
print("----------------Assignment Operator---------------------------")

c = 0
d = 1

c+=d # c=c+d
print(c)

e = 0
f = 2
e-=f # e=e-f
print(e)

print("-----------------------------------------------------------------------------")
print("----------------Logical Operator---------------------------")

var1 = 30
var2 = 60

var3 = 2
var4 = 1

out = (var1 > var2) or (var3 > var4)  # Anyone of condition is true it will return True.
print(out)

out = (var1 < var2) or (var3 > var4)  # if both condition is ture then return True.
print(out)

out = (var1 > var2) or (var3 < var4) # if both condition is wrong then return False.
print(out)

print("-----------------------------------------------------------------------------")

out = (var1 > var2) and (var3 > var4)  # Anyone of condition is false it will return False.
print(out)

out = (var1 < var2) and (var3 > var4)  # if both condition is ture then return True.
print(out)

out = (var1 > var2) and (var3 < var4) # if both condition is wrong then return False.
print(out)

print("-----------------------------------------------------------------------------")

out = not(var1 < var2) # It makes true to false and false to true
print(out)

print("-----------------------------------------------------------------------------")
print("----------------Membership Operator---------------------------")

Tuples=("Linux","Vagrant","Bash Scripting","AWS","Jenkins","Python","Ansible")
ans = "Linux" in Tuples # in , membership Operator which traverse in range or any data structure(like list or tuples) to find particular asked element ,if found it give True otherwise False
print(ans)

ans = "Linux" not in Tuples # if oppositely asked that this element is not in this range or data structure , on that basis it gives answer True or False
print(ans)

print("-----------------------------------------------------------------------------")
print("----------------Identity Operator---------------------------")

num1 = 12
num2 = 15

out = (num1 is num2) # variable 1 is equal to variable 2
print(out)

out = (num1 is not num2) # variable 1 is not equal to variable 2
print(out)