# 1. print a list of even numbers
numbers = [1,2,3,4,5,6,7,8,9,0]
even_numbers = []
for number in numbers: 
	if( number % 2 == 0):
		even_numbers.append(number)
print(even_numbers)

# 2. iterate over a list of strings:
planets = ['budh','shukro', 'prithibi', 'mangal']
for planet in planets:
	print(planet)

# 3. iterate over a string:
month = 'November'
print(month, "is spelled: ")
for x in month:
	print(x)
	
# 4. break statement
x = 1
while x <= 10:
	if x == 5:
		break
	print("x is now: ", x)
	x +=1
	
# 5. continue statement
# print all the od numbers between 1 - 20, except those are multiple of 3
for no in range(1, 21):
	if (no % 2 != 0):
		if(no % 3 == 0):
			continue
		print(no)