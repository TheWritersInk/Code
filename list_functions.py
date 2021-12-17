lucky_numbers = [4, 15, 8, 16, 23, 42]
friends = ['Bob', 'Pedro', 'Alice', 'Alice', 'Oscar', 'Toby']
#friends.extend(lucky_numbers) # Add two lists together
#friends.append("Creep") # Add additinal to end of list
#friends.insert(1, 'bone') # Insert into a specific index place
#friends.remove('Bob') # Remove specific item
# friends.clear()
# friends.pop() # Clear last thing from list
# friends.count('Alice')
friends.sort() # Alphabetically sort
lucky_numbers.sort()
lucky_numbers.reverse()

friends2 = friends.copy() # Copy friends list to friends 2

print(friends2)
print(friends.index('Alice')) # Tell the place of Alice
print(lucky_numbers)