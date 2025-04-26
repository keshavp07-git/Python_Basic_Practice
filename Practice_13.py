#Keywords Arguments , some time we have two types of variables one int and one string then if we pass them into function they throw error if
# they are not in order so by defining their type with their in argument section in the function then will not throw error.
def vac_feed(vac,effi):
    print(f"Vaccine name is {vac} and Efficiency is {effi}")
    if (effi > 50) and (effi <=75):
        print("This vaccine needs more trials")
    elif (effi > 75) and (effi < 90):
        print("This vaccine is mild effective")
    elif (effi >= 90):
        print("This vaccine is good effective")
    else :
        print(" can't take shot")

vac_feed("Pfizer",95)
print("----------------------------------------------------------------------------------------------------")
# vac_feed(95,"Pfizer") -- This will throw error because argument type is not in order so we can do ,
vac_feed(effi=96 , vac="Covaxin")

