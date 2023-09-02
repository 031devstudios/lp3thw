# Imports argv function from the 'sys'tem
from sys import argv

# Script is default, makes a variable that argv will pass info into
script, filename = argv

# Declares 'txt' variable and uses the open() function with filename argv passed into it.
txt = open(filename)

# Prints a f-string with filename from argv
print(f"Here's your file {filename}:")
# Prints the contents of txt while using the .read() function to print out the contents of the file
print(txt.read())
txt.close()

# Prints a string
print("Type the filename again:")
# Declares variable and prompts the user for an input
txt_again = input('> ')
# Declares a variable and uses the open() function to open the file
file_again = open(txt_again)

# Prints the content of the file opened on the previous line.
print(file_again.read())
file_again.close()