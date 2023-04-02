#Chapter 3 List excercises
guest_list = ['Javed', 'Waled', 'Diana']
print(f"Hello, {guest_list[0]}! You are invited to the dinner.")
print(f"Hello, {guest_list[1]}! You are invited to the dinner.")
print(f"Hello, {guest_list[2]}! You are invited to the dinner. \n")

#the guest that can't make it.
print(f"Sorry, our guest {guest_list[1]} cannot make it to the dinner. \n")

guest_list[1] = 'Naeem'

#modifying the guest list
guest_list = ['Javed', 'Khalil', 'Diana']
print(f"Hello, {guest_list[0]} we are looking forward to seeing you on the dinner tonight. ")
print(f"Hello, {guest_list[1]} we are looking forward to seeing you on the dinner tonight.")
print(f"Hello, {guest_list[2]} we are looking forward to seeing you on the dinner tonight. \n")

#informing everyone about bigger table
print("Hello guests! we just found a bigger table. \n")

#adding guest using insert() method
guest_list.insert(0, 'Albert')
guest_list.insert(2, 'Daniel')
guest_list.append('Khan')

#Sending new set of invites to all guests
print(f"Hello {guest_list[0]}, we are looking forward to see you on dinner.")
print(f"Hello {guest_list[1]}, we are looking forward to see you on dinner.")
print(f"Hello {guest_list[2]}, we are looking forward to see you on dinner.")
print(f"Hello {guest_list[3]}, we are looking forward to see you on dinner.")
print(f"Hello {guest_list[4]}, we are looking forward to see you on dinner.")
print(f"Hello {guest_list[5]}, we are looking forward to see you on dinner.\n")

#table won't arrive on time, space for only 2 guests.
print(f"Hi everyone! sorry my dinner table won't arrive on time so I only have space for 2 guests. \n")

#using pop() to remove the rest of the guests
removed_guests = guest_list.pop()
print(f"I am sorry {removed_guests}, you are not invited anymore.")
removed_guests = guest_list.pop()
print(f"I am sorry {removed_guests}, you are not invited anymore.")
removed_guests = guest_list.pop()
print(f"I am sorry {removed_guests}, you are not invited anymore.")
removed_guests = guest_list.pop()
print(f"I am sorry {removed_guests}, you are not invited anymore.\n")

#msg the two people still invited 
print(f"Hi {guest_list[0]} you are still invited for tonight's dinner.")
print(f"Hi {guest_list[1]} you are still invited for tonight's dinner. \n")

#using del to remove the remaining of the 2 guests 
del guest_list[1]
del guest_list[0]

print(guest_list)







