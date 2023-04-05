#Try It Yourself

#4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these
#pizza names in a list, and then use a for loop to print the name of each pizza.
#•	 Modify your for loop to print a sentence using the name of the pizza
#instead of printing just the name of the pizza. For each pizza you should
#have one line of output containing a simple statement like I like pepperoni
#pizza.
#•	 Add a line at the end of your program, outside the for loop, that states
#how much you like pizza. The output should consist of three or more lines
#about the kinds of pizza you like and then an additional sentence, such as
#I really love pizza!

pizzas = ['pepperoni', 'cheese', 'vagi']
for pizza in pizzas:
	print(f"I like {pizza.title()} pizza.")
print("I cannot begin to even tell you how much I like these pizzas.\nAs you can see they are all my favorites.\nAnd I really love them.\n")

print("-------------------------------------------------------------------------------------------------------------------------------------------")

# 4-2. Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to
# print out the name of each animal.
# •	 Modify your program to print a statement about each animal, such as
# A dog would make a great pet.
# •	 Add a line at the end of your program stating what these animals have in
# common. You could print a sentence such as Any of these animals would
# make a great pet!

animals = ['dogs', 'wolves', 'Hyenas']
for animal in animals:
	print(f"A {animal.title()} would make an awesome pet.")
print("All of these animals are great pets if you can have them.")