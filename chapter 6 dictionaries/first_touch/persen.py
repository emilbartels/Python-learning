#“6-1. Person: 
# Use a dictionary to store information about a person you know. 
# Store their first name, last name, age, and the city in which they live. 
# You should have keys such as first_name, last_name, age, and city. 
# Print each piece of information stored in your dictionary.”

person = {'first_name': 'Liv', 'last_name': 'Sonne-Clifford', 'age': 20, 'city': 'Tårnby', 'boyfriend': 'Emil'}
print(f'Her first name is {person["first_name"]}')
print(f'Her last name is {person["last_name"]}')
print(f'Her full name is {person["first_name"]} {person['last_name']}')
print(f'She is {person['age']} years old and lives in {person["city"]}')

# brug af get()
boyfriend = person.get('boyfriend', 'There is no boyfriend, as she is alone.')
print(f'She has a awesome boyfriend {boyfriend}')