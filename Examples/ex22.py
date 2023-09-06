print() # prints a string

# comment // # makes a comment and wont run in code

variable = "Hello World" # declares a varaible and writes a value to it

unit = variable + 10 # does math when declaring a variable

print(variable.format(unit)) # prints a formatted variable with another varialbes format/value

x = "string \n text" # \n tell python to print on a new line

y = "string \t text" # \t tell ppython to tab a line / indent

input("Enter some text here.") # gets an input from the user -> string

print(f"This is a formatted string {x} {y}") # prints a f-string with value x, y

from sys import argv # uses argv to pass arguments into the script
script, first, second, third = argv #

txt = open(variable) # gets the handle for a file in order to open it
print(txt.read()) # print the contents of the file that was previously opened
txt.close() # closes the file once done with it

target = open(variable, 'w') # opens a file in write mode so data can be written to it
target.write(f"{unit}\n{x}\n{y}") # writes the data from the arguments into that "target"

int() # converts a varialbe to an interger data type

float(input()) # allows the user to input a number with a decimal point

len() # returns the length of data in bytes

from os.path import exists # used to check if a file exsists already and returns a bool

def function(x, y): # defines a custom fuction and accepts two arguments / parameters
    print(x, y) # the codes that will run when you call the function
    return x, y # returns the value of x and y

current_line = 1 # make a variable equal to a value
current_line += 1 # increments the variable by 1

x.seek(0) # moves the cursor position in a file

x.readline() # reads a specified line in a file