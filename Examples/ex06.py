# Declares the varialbe "types_of_people" and makes it equal to 10.
types_of_people = 10
# Declares the variable "x" and makes it an f-string.
x = f"There are {types_of_people} types of people."

# Declares the varialbe "binary" and makes it equal to a string.
binary = "binary"
# Declares the varialbe "do_not" and makes it equal to a string.
do_not = "don't"
# Declares the variable "y" and makes it an f-string.
y = f"Those who know {binary} and those who {do_not}."

# Prints the value of "x"
print(x)
# Prints the value of "y"
print(y)

# Print a f-string formatted with the value of "x"
print(f"I said: {x}")
# Print a f-string formatted with the value of "y"
print(f"I also said: '{y}'")

# Decalres a variable "hilarious" and sets it to False
hilarious = False
# Delcares a variable "joke_evaluation" and makes it equal to a f-string.
joke_evaluation = "Isn't that joke so funny?! {}"

# Print the variable "joke_evaluation" and formats it with the variable "hilarious"
print(joke_evaluation.format(hilarious))

# Declares variable "w" and makes equal to string.
w = "This is the left side of..."
# Declares variable "ee" and makes equal to string.
e = "a string with a right side."

# Prints varaible "w" and prints variable "e" afterwards
print(w + e)