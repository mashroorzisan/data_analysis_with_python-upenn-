# 1. initializing a list of random strings and integers
list1 = ['1',2,'dog', 'cat']
print(list1)

# 2. get length of the list
print(len(list1))

# 3. get the second item of the list
print(list1[1])

# 4. get the 5th item of the list
# print(list1[4]) #indexError

# 5. append items to the list
list1.append('hello')
print(list1)

# 6. pop items from the list
list1.pop()
print(list1)

# 7. checking if an item exists or not
print('cat' in list1)