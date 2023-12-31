# Creating a list
fruits = ["apple", "banana", "cherry"]

# Accessing elements
print(fruits[0])  # Output: apple, zero refers to the first element

# Modifying elements
fruits[1] = "kiwi" # Replacing banana with kiwi
print(fruits)  # Output: ["apple", "kiwi", "cherry"]

# Adding elements
fruits.append("orange") # Adds orange to the end of the list
print(fruits)  # Output: ["apple", "kiwi", "cherry", "orange"]

# Removing elements
fruits.remove("kiwi") # Removes kiwi from the list
print(fruits)  # Output: ["apple", "cherry", "orange"]
