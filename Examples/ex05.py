name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # pounds
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

my_weight_in_kgs = weight * 0.453592
my_height_in_cm = height * 2.54

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {round(my_height_in_cm, 1)} cm tall.")
print(f"He's {weight} pounds heavy.")
print(f"He's {round(my_weight_in_kgs, 1)} kgs heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}")