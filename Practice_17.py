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

exitcode= os.system("grep science etc/group") # Search for science group if found it will give zero or not than non-zero message
if exitcode !=0: # compare the zero and non-zero so that we can or not
    print("Group Science Doesn't exists..Adding it")
    print("--------------------------------------------------------------------------------------------")
    print()
    os.system("groupadd science") # Command used to add group and we gave the name also here like science
else:
    print("Group already exists")
    print("--------------------------------------------------------------------------------------------")
    print()

for user in userlist: # Again do iteration to add user to group science
    print("Adding user {} to the science group".format(user)) # Formatting the message which user adding to which group
    print("Adding user to group....")
    print("--------------------------------------------------------------------------------------------")
    os.system("usermod -G science {}".format(user)) # Command to add all find user not exists in group science
    print("---------------------------------------------------------------------------------------------")
    print()



