#write functions here, don't add input('') statements here!
global_var = 5

# Function to modify the global variable without parameters
def use_global():
    global global_var  # Declare that we want to use the global variable
    global_var += 10  # Modify the global variable by adding 10

# Call the function to modify the global variable
use_global()

# Display the updated value of the global variable
print("Updated global_var:", global_var) 