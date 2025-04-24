# For Loop
from time import sleep

PLANET = "Earth"
for i in PLANET:
    print("The value if is now",i)

print("---------------------------------------------------------------------------")

VACCINES = ("Pfizer", "Moderna", "Sputnik v", "Covaxin" , "AstraZeneca")
for vac in VACCINES:
    print(f"{vac} is used to fight against covid-19")

print("----------------------------------------------------------------------------")

VACCINES = ("Pfizer", "Moderna", "Sputnik v", "Covaxin" , "AstraZeneca")
for vac in VACCINES:
    print()
    print("I think these are Dangerous ")
    for i in vac:
        print(i)

print("--------------------------------------------------------------------------------")

# While Loop
x=0
while x<=10:
    print("The value of X is now :-",x)
    x+=1
print("--------------------------------------------------------------------------------")

import time
x = 2
while True:
    print("The value of X is now :-",x)
    print("Looping")
    x+=2
    time.sleep(1)

