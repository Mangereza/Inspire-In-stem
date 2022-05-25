#!/usr/bin/python

# A dictionary is a collection of key value pairs
#synatx : dictinary = {'key':'value'}
#names='john Mary'
colors={'color':'red'}
vehicle={'type':'toyota','plate number':'KDH254L'}
#print(type(names)) #we use the type method to read the data type
#accessing values in a dictionary
#print(vehicle['type']) #you can access the value and its element
person={'name':'John','Gender':'Male','tel_number':'+254743287653','address':'Tom mboya street'}
person['age']='22'
person['color']='Navy blue'
#print(type(person))
#print(person)
#deleting an item from a list
del person['tel_number']
print(type(person))
print(person)
#looping over dictionaries
for key, value in person.items():
    print(f"{key}:{value}")