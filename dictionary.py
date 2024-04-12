person = {
    'name'  :'Zed',
    'age'   : 39,
    'height': 6*12+2
}
print(type(person))

# 1. get value by using brackets []
print(person['name'])

# 2. alternative method is to use built in get method
print(person.get('height'))

# 3. get function is good to use, in case the key DNE
# this gives keyError
# uncomment the line below to test the code
# print(person['address']) 
print(person.get('address')) # as you can see no error and also returns none

# 4. dictionaries are mutable
person['name'] = 'John'
person['age'] += 1
person['address'] = 'somewhere between nowhere'
print(person.get('address'))

# 5. checking if a key exists:
print('address' in person)
print('college' in person)

# 6. delete elements using del keyword:
del person['address']
print(person.get('address'))

# 7. or delete the whole dictionary
# del person
# print(person.get('address'))

# 8. dictionaries can include other dictionaries or lists as values:
person['siblings'] = ['cory','tylor', 'jamie', 'ron']
person['siblings'].append('Betsy')
print(person)

# 9. we can add new attributes with data values using update keyword
person_attrib = {'marital status':True, 'nationality':'Bangladeshi','Religion': 'Catholic'}
person.update(person_attrib)
print('#######################')
print(person)

