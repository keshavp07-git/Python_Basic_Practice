#Variable length argument are used when we don't know about length of arguments , and we can provide any no. of arguments so this type of argument helps us
# When we used it we get Tuple where all argument stored (*args).
def oder_food(item,*args): # item take one item and *args is tuple take multiple items
    print(f"You have ordered,{item}") # single item printed
    for i in args: # iteration everything go from *args to i
        print(f"You have ordered,{i}") # Now printing stored in i
    print("Your Food Will be Delivered soon")
    print("Enjoy the part")

oder_food("Pizza","Burger","MoMos","Coldrink")