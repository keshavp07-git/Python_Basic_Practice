#!/usr/bin/python3
import os
userlist = ("x", "y", "z" , "w") # userlist that we have add.
print("Adding user......")
print("---------------------------------------------------------------------------------------------------")
for user in userlist: # We iterate into the list and store into user variable
    exitcode=os.system("id {}".format(user)) # When user not exist linux return code so we use exit code to check user exist or not
    # variable return string with quotes which will not acceptable "x" , so we use .format(user) method to remove quotes for that
    # we left empty space with {} to replace. it will be like id : 'x' after format......Auto format
    if exitcode !=0: # Checking if user is not equal to 0 it means we can add it , Not already exists
        print("User {} doesn't exist , Adding the user......".format(user)) # Just printing it with .format(user) to replace variable in quotes...Auto format
        print("--------------------------------------------------------------------------------------------")
        print()
        os.system("useradd {}".format(user)) # This will add user in linux with useradd command and {} remove the quotes by using .format(user)...Auto format
    else:
        print("User already exists") # Else Print already exists
        print("--------------------------------------------------------------------------------------------")
        print()

