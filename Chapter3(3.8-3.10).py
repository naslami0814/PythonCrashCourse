#3-8. Seeing the World: Think of at least five places in the world you’d like to visit.


#Store the locations in a list. Make sure the list is not in alphabetical order.
visit_locations = ['Malta', 'Singapore', 'Australia', 'Italy', 'UK']
print(visit_locations)

#Use sorted() to print your list in alphabetical order without modifying the actual list.
print(sorted(visit_locations))

#Show that your list is still in its original order by printing it
print(visit_locations)

#Use sorted() to print your list in reverse alphabetical order without changing the order of the original list
print(sorted(visit_locations,reverse=True))

#Show that your list is still in its original order by printing it again.
print(visit_locations)


#Use reverse() to change the order of your list. Print the list to show that its order has changed.
visit_locations.reverse()
print(visit_locations)


#Use reverse() to change the order of your list again. Print the list to show it’s back to its original order
visit_locations.reverse()
print(visit_locations)

#Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
visit_locations.sort()
print(visit_locations)

#Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.
visit_locations.sort(reverse=True)
print(visit_locations)


#3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 through 3-7 (page 46), use len() to print a message indicating the number of people you are inviting to dinner.
guest_list = ['Javed', 'Waled', 'Diana']
print(f"Hello, {guest_list[0]}! You are invited to the dinner.")
print(f"Hello, {guest_list[1]}! You are invited to the dinner.")
print(f"Hello, {guest_list[2]}! You are invited to the dinner. \n")

print(len(guest_list))
