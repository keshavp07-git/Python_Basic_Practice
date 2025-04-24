
planet1 = "Closest to sun"
print("--------------------------------------------------------------------------")
print(planet1)
print("--------------------------------------------------------------------------")
print(planet1[0])
print(planet1[1])
print(planet1[2]) # Retrieving using +ve index , from starting.
print("---------------------------------------------------------------------------")
print(planet1[-1])
print(planet1[-2])
print(planet1[-3]) # Retrieving using -ve index , from Back , negative index can't start from 0 , if we use -0 , we redirect to 1st element.

# Fetching data from data structure within a range called Slicing.
# Slicing a string , get a substring from a string.
print("---------------------------------------------------------------------------")
print("-------------Retrieving Data-------------")
print("---------------------------------------------------------------------------")
print(planet1[0:7]) # Giving range to retrieve data , before : -- starting and after : -- ending , exclude last one like 7th position , which is whitespace
print("---------------------------------------------------------------------------")
print(planet1[:]) # Giving nothing range , it will automatically take 0 to -1
print("---------------------------------------------------------------------------")
print(planet1[:7]) # Automatically take 0 for starting and we defined end that is 7
print("---------------------------------------------------------------------------")
print(planet1[11:]) # It takes 11 for starting and automatically defined end that -1


print("---------------------------------------------------------------------------")
print("--------Slicing Tuples----------")
print("---------------------------------------------------------------------------")
Tuples=("Linux","Vagrant","Bash Scripting","AWS","Jenkins","Python","Ansible")
print(Tuples)
print("---------------------------------------------------------------------------")
print(Tuples[0:4]) # Exclude 4th one , count from 0 to 4 and give 0 ,1 ,2 ,3 and exclude 4th position
print("---------------------------------------------------------------------------")
print(Tuples[2:5]) # Count from 2 index to 4 and exclude 5
print("---------------------------------------------------------------------------")
print(Tuples[2:5][0][5:11]) # Count from 2 index to 4 and exclude 5 then , Now it returns a list of 3 element so , we choose 0 for 1st element which is Bash Scripting ,
# In Bash Scripting we choose 5 to 11 which gives Script and exclude last 11th element.
print("---------------------------------------------------------------------------")
print(Tuples[2:5][0][5:11][-1]) # we can do more slice our word "Script" so -1 give "t".
print("---------------------------------------------------------------------------")
print("-----------Slicing List-----------")
print("---------------------------------------------------------------------------")
List=["Linux","Vagrant","Bash Scripting","AWS","Jenkins","Python","Ansible"]
print(Tuples)
print("---------------------------------------------------------------------------")
print(Tuples[0:4]) # Exclude 4th one , count from 0 to 4 and give 0 ,1 ,2 ,3 and exclude 4th position
print("---------------------------------------------------------------------------")
print(Tuples[2:5]) # Count from 2 index to 4 and exclude 5
print("---------------------------------------------------------------------------")
print(Tuples[2:5][0][5:11]) # Count from 2 index to 4 and exclude 5 then , Now it returns a list of 3 element so , we choose 0 for 1st element which is Bash Scripting ,
# In Bash Scripting we choose 5 to 11 which gives Script and exclude last 11th element.
print("---------------------------------------------------------------------------")
print(Tuples[2:5][0][5:11][-1]) # we can do more slice our word "Script" so -1 give "t".
print("---------------------------------------------------------------------------")
print("-----------Slicing Dictionary-------------")
print("---------------------------------------------------------------------------")
Dict = {"DevOps":["AWS","Jenkins","Python","Ansible"],"Essentials":("Linux","Vagrant","Bash Scripting")}
print(Dict)
print(Dict["DevOps"][2]) #Slicing Value from Key , From key DevOps get value Python
print(Dict["DevOps"][2][0:2]) # Slicing value , From value slice Py
