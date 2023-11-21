# Creating a tuple
fruits_tuple = ('apple', 'orange', 'banana')

# Accessing elements in a tuple
print("First fruit:", fruits_tuple[0])  # Output: 'apple'

# Attempting to modify a tuple (this will raise an error)
# fruits_tuple[0] = 'pear'  # Uncommenting this line will result in a TypeError

# Concatenating tuples
more_fruits = ('grape', 'kiwi')
combined_fruits = fruits_tuple + more_fruits
print("Combined fruits:", combined_fruits)  # Output: ('apple', 'orange', 'banana', 'grape', 'kiwi')

# Slicing a tuple
sliced_tuple = combined_fruits[1:4]
print("Sliced tuple:", sliced_tuple)  # Output: ('orange', 'banana', 'grape')

# Tuple unpacking
first, second, *rest = combined_fruits
print("First element:", first)  # Output: 'apple'
print("Second element:", second)  # Output: 'orange'
print("Rest of the elements:", rest)  # Output: ['banana', 'grape', 'kiwi']

# Finding the index of an element in a tuple
index_of_banana = combined_fruits.index('banana')
print("Index of 'banana':", index_of_banana)  # Output: 2

# Counting occurrences of an element in a tuple
count_of_orange = combined_fruits.count('orange')
print("Count of 'orange':", count_of_orange)  # Output: 1

# Checking if an element is in a tuple
print('kiwi' in combined_fruits)  # Output: True
print('pear' in combined_fruits)  # Output: False
