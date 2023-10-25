# create a mapping of state to abberiation
states = {
    'Oregan': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

#create a basic set of states and some cities in them
cities = {
    'CA': 'San Franciso',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Port Land'

# print out some cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# print some states
print('-' * 10)
print("Michigan's abberviation is: ", states['Michigan'])
print("Florida's abberviation is : ", states["Florida"])

# do it by using the state then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every state abberviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abberivation {abbrev}")

# print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abberviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
# safely get an abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does Not Exsist')
print(f"The city for the state 'TX' is: {city}")