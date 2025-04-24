name = "sars_cov_2"
disease = "covid19"

print("The name of virus is", name)
print("The name of virus is {}".format(name))
print("{} is the name of virus.".format(name))
print("The name of virus is {} and it causes {}".format(name, disease))
print(f"The name of virus is {name} and it causes {disease}")

# Different way to Print replacing variables with actual values using f and .format() method

#Concatination
print("Concatinate Method , The name of virus is" +" " +name)