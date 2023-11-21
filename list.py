# Creating a list
fruits = ['apple', 'orange', 'banana', 'grape']

# Accessing elements in a list
print(fruits[0])  # Output: 'apple'
print(fruits[2])  # Output: 'banana'

# Modifying elements in a list
fruits[1] = 'pear'
print(fruits)  # Output: ['apple', 'pear', 'banana', 'grape']

# Adding elements to a list
fruits.append('kiwi')
print(fruits)  # Output: ['apple', 'pear', 'banana', 'grape', 'kiwi']

# Removing elements from a list
removed_fruit = fruits.pop(2)
print(fruits)  # Output: ['apple', 'pear', 'grape', 'kiwi']
print("Removed fruit:", removed_fruit)  # Output: 'banana'

# Iterating through a list
for fruit in fruits:
    print(fruit)

# Checking if an element is in the list
print('kiwi' in fruits)  # Output: True
print('melon' in fruits)  # Output: False

# Creating a list of squares of numbers from 0 to 9 using a for loop
squares_using_loop = []
for num in range(10):
    squares_using_loop.append(num ** 2)

print("Using a for loop:", squares_using_loop)

# Creating the same list using a list comprehension
squares_using_comprehension = [num ** 2 for num in range(10)]

print("Using list comprehension:", squares_using_comprehension)


even_numbers = [num for num in range(10) if num % 2 == 0]
print("Even numbers:", even_numbers)
