#Nested Loops refers loops inside loops
rows = 5
for i in range(rows):
    for j in range(i + 1):
        print("*", end=" ")
    print()

#This will print a triangle of stars