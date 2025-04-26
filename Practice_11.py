print("----------------------------------------------------------------------------------------------------------------------------------------")
# Built in Methods for String (string is immutable)
from email.message import Message

message = "corona vaccines is ready to use most of them are very effective"
print(message.capitalize()) # Capital first letter of corona , but as we know string is immutable , we can check by printing message again.
print(message) # Confirmed
Message = message.capitalize() # Here we stored in another variable then we again print the message then it's worked.
print(Message) # Printing another Variable
print(message.upper()) # Whole text will be in uppercase
print(message.lower()) # whole text will be in lowercase
print(message.islower()) # Check text is in lower case on not then give boolean value
print(message.isupper()) # check for upper case
print(message.find("ready")) # search any string and give starting index value , give value 19 from index value 19 - ready start and till 25 it exists.
print(message[19:25]) # Printing ready after searching index value
print(message.find("not")) # Find it but doesn't exist so return -1

print("--------------------------------------------------------------------------------------------------------------------------------------")

# Operation with Tuple , doing less methods because it is immutable
seq=("192","168","10","1") # Now doing some operation like joining with different characters in Tuples
print(".".join(seq)) # Join with dot
print("/".join(seq))
print("-".join(seq))


print("--------------------------------------------------------------------------------------------------------------------------------------")
# Operation with List
country = ["India","US","UK"]
print(country)
country.append("UAE") # Add into List
print(country)
country.extend(["China", "Japan" , "Russia" , "Germany"]) # Add or Join existing List
print(country)
country.insert(2,"France") # Add at choice placed
print(country)
country.pop()
print(country) # Remove element from back
country.pop(5)
print(country) # Remove from choice place
print("--------------------------------------------------------------------------------------------------------------------------------------")
# Operation with Dictionary
emp1 = {"Name":"Santa" , "Skill":"BlockChain" , "code":1024}
print(emp1.keys()) # Print all the keys
print(emp1.values()) # Print all the values
emp1.clear() # Clear the Dictionary
print(emp1)
print("--------------------------------------------------------------------------------------------------------------------------------------")

# dir() --- It tell all available methods for a variable
print(dir(message)) # --- It print all available methods for message variable
print(dir("")) # for String
print(dir({})) # for Dictionary
print(dir([])) # for List
print(dir(())) # Tuple

print("--------------------------------------------------------------------------------------------------------------------------------------")