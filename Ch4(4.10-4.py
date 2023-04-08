# 4-10. Slices: Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:



# •	 Print the message, The first three items in the list are:. Then use a slice to
# # print the first three items from that program’s list.
players = ['jeremiah', 'nadeem', 'suriya', 'maylin', 'griselda', 'lee', 'anwar']
print("The first 3 players are:")
for player in players[:3]:
	print(player.title())


print("-------------------------------------------------------------------------")


# •	 Print the message, Three items from the middle of the list are:. Use a slice
# to print three items from the middle of the list.
print("The three players from the middle are:")
for player in players[2:5]:
	print(player.title())


print("-------------------------------------------------------------------------")


# •	 Print the message, The last three items in the list are:. Use a slice to print
# the last three items in the list.
print("The last 3 players will be:")
for player in players[-3:]:
	print(player.title())

print("-------------------------------------------------------------------------")


# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
# (page 60). Make a copy of the list of pizzas, and call it friend_pizzas.
# Then, do the following:
pizzas = ['pepperoni', 'cheese', 'vagi']
friend_pizzas = pizzas[:]

#Add a new pizza to the original list.
pizzas.append('new pizza')

#•	 Add a different pizza to the list friend_pizzas.
friend_pizzas.append('friends pizza')


# #Prove that you have two separate lists. Print the message, My favorite
# pizzas are:, and then use a for loop to print the first list. Print the message,
# My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.
print("My favorite pizzas are:")
for pizza in pizzas:
	print(pizza.title())

print("My friend's favotire pizzas are:")
for pizza in friend_pizzas:
	print(pizza.title())


print("-------------------------------------------------------------------------")

#Excersize 4.12 is basically everything we have done in this tutorial.

