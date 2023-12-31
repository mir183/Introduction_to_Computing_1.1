# Function Without Arguments and Return Value
def greet():
    print("Hello, welcome!")

greet()

# Function With Arguments but Without Return Value
def greet_with_name(name):
    print(f"Hello, {name}!")

greet_with_name("Alice")

# Function With Arguments and Return Value
def add_numbers(x, y):
    return x + y

result = add_numbers(5, 3)
print(result)  # Output: 8

# Function With Default Arguments
def power(x, exponent=2):
    return x ** exponent

result1 = power(2)
result2 = power(2, 3)

# Function With Variable Number of Arguments (*args)
def sum_all(*args):
    return sum(args)

total = sum_all(1, 2, 3, 4)

# Function With Variable Number of Keyword Arguments (**kwargs)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Bob", age=30, city="London")
