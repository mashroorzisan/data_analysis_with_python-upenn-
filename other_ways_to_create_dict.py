# other ways to create dictionary
# 1. initializing an empty dictionary:
courses = {}
course_name = input()
courses[course_name] = 'intro to programming'
courses.update({'cis232': 'Big data'})
print(courses.get('cit348'))
print(courses)

# 2. create a dictionary from a list of tuples using the dict function:
translation = dict([
    (1, 'uno'), 
    (2,'dos'),
    (3,'tres')
    ])
print(type(translation))
print(translation)

couples = dict([
    ('salekh','salekha'), 
    ('rahim','rahima'), 
    ('karim','karima')
])
print(couples)

# 3. create a dictionary from two separate list:
key_lst = ['joey', 'fred', 'kathy']
value_lst = [ 6, 4, 3]
# then make a list of zip using zip function
zipped = zip(key_lst, value_lst)
print(zipped)
print(type(zipped))
# then create a dictionary from the zip
kids = dict(zipped)
print(kids)
print(type(kids))