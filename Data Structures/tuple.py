# Creating a tuple
colors = ("red", "green", "blue")

# Accessing elements
print(colors[0])  # Output: red

# Immutable nature (this will result in an error)
#colors[1] = "yellow"
'''It is not possible to modify a tuple's elements. 
This is because tuples are immutable, 
which means that you cannot change a tuple's content once it is created.'''

# Concatenating tuples
new_colors = colors + ("yellow", "purple")
print(new_colors)  # Output: ("red", "green", "blue", "yellow", "purple")
