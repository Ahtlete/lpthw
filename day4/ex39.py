#create a mapping
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'NY',
    'Michigan': 'MI'
}

#create a basic set of states
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print some cities
print('-' * 10)
print("NY State has:", cities['NY'])
print("OR State has:", cities['OR'])

print('-' * 10)
print("Michigan has:", cities[states['Michigan']])
print("Florida has:", cities[states['Florida']])

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

#now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")