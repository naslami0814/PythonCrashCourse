# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.
numbers = list(range(1,21))
print(numbers)

print("-------------------------------------------------------------------------------")

# 4-4. One Million: Make a list of the numbers from one to one million, and then
# use a for loop to print the numbers. (If the output is taking too long, stop it by
# pressing ctrl-C or by closing the output window.)
one_million = list(range(1,1000001))
for value in one_million:
	print(value)

print("-------------------------------------------------------------------------------")

# 4-5. Summing a Million: Make a list of the numbers from one to one million,
# and then use min() and max() to make sure your list actually starts at one and
# ends at one million. Also, use the sum() function to see how quickly Python can
# add a million numbers.
one_mill = list(range(1,1000001))
print(min(one_mill))
print(max(one_mill))
print(sum(one_mill))



# 4-6. Odd Numbers: Use the third argument of the range() function to make a list
# of the odd numbers from 1 to 20. Use a for loop to print each number.
for num in range(1,21,2):
	print(num)

print("-------------------------------------------------------------------------------")


# 4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
# print the numbers in your list.
threes = list(range(1,11))
for three in threes:
	multiples = three * 3
	print(multiples)

print("-------------------------------------------------------------------------------")

# 4-8. Cubes: A number raised to the third power is called a cube. For example,
# the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
# is, the cube of each integer from 1 through 10), and use a for loop to print out
# the value of each cube.
cubes = list(range(1,11))
for cube in cubes:
	rasied = cube ** 3
	print(rasied)

print("-------------------------------------------------------------------------------")


# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the
# first 10 cubes.
cubes = [value**3 for value in range(1,11) ]
print(cubes)