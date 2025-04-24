for i in "DEVOPS": # do iteration
    print(i) # print the element
    if i == "O": # if founded
        print("Data Found") # print data found
        break # break the loop and exit
print("Exited-----------------------------------------------------")


for i in "DEVOPS": # do iteration
    if i == "O": # if found element
        print("value found") # print value founded
        continue # and use continue skip that iteration and continue to next one
    print(f"The value is {i}") # printing the value
print("Exited------------------------------------------------------")