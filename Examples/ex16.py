from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit Ctrl-C (^C).")
print("If you do want that hit RETURN.")

input('?')

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate

print("I'm going to ask you for three lines.")
line1 = input("Line1: ")
line2 = input("Line2: ")
line3 = input("Line3: ")

print("I'm going to write these to the file.")
'''
target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')
'''

target.write(f"{line1}\n{line2}\n{line3}\n")
              
print(f"And finally we close the file {filename}")
target.close()