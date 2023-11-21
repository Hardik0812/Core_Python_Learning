# Creating a dictionary
person = {
    'name': 'John',
    'age': 30,
    'city': 'New York',
    'email': 'john@example.com'
}

# Accessing values in a dictionary
print("Name:", person['name'])  # Output: John
print("Age:", person['age'])    # Output: 30

# Modifying values in a dictionary
person['age'] = 31
print("Updated age:", person['age'])  # Output: 31

# Adding a new key-value pair
person['gender'] = 'Male'
print("Updated dictionary:", person)

# Removing a key-value pair
removed_email = person.pop('email')
print("Dictionary after removing email:", person)
print("Removed email:", removed_email)

# Iterating through keys and values
for key, value in person.items():
    print(f"{key}: {value}")

# Checking if a key is in the dictionary
print('city' in person)  # Output: True
print('phone' in person)  # Output: False

# Getting a default value for a key
phone = person.get('phone', 'N/A')
print("Phone:", phone)

# Clearing all key-value pairs from the dictionary
person.clear()
print("Empty dictionary:", person)


# Creating a dictionary of squares for numbers from 0 to 9 using a for loop
squares_dict_using_loop = {}
for num in range(10):
    squares_dict_using_loop[num] = num ** 2

print("Using a for loop:", squares_dict_using_loop)

# Creating the same dictionary using a dictionary comprehension
squares_dict_using_comprehension = {num: num ** 2 for num in range(10)}

print("Using dictionary comprehension:", squares_dict_using_comprehension)

even_squares_dict = {num: num ** 2 for num in range(10) if num % 2 == 0}
print("Even squares dictionary:", even_squares_dict)
