import random

VACCINES = ["Pfizer", "Moderna", "Sputnik v", "Covaxin" , "AstraZeneca"]
random.shuffle(VACCINES) # shuffle the whole list
LUCKY = random.choice(VACCINES) # give one element from list
print(LUCKY)

for vac in VACCINES:  # taking all elements from list by iterating
    if(vac == LUCKY): # compare the lucky one exist in vac elements which we get by iterating
        print("--------------------------------------------")
        print(f"------{LUCKY} Successfully Tested----------") # And that one exist in both lucky or iterated variable which vac then it is Successfully Tested
        print("--------------------------------------------")
        break # Break other iteration because we matched the elements already
print("----ELSE FAILED IN TEST----") # this gives us the message for other vaccines