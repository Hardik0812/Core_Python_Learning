# Creating a set
fruits_set = {'apple', 'orange', 'banana', 'apple'}  # Note: 'apple' is repeated but sets only store unique elements
print("Initial set:", fruits_set)  # Output: {'orange', 'banana', 'apple'}

# Adding elements to a set
fruits_set.add('kiwi')
print("Set after adding 'kiwi':", fruits_set)  # Output: {'orange', 'banana', 'apple', 'kiwi'}

# Removing an element from a set
fruits_set.remove('orange')
print("Set after removing 'orange':", fruits_set)  # Output: {'banana', 'apple', 'kiwi'}

# Checking if an element is in a set
print('banana' in fruits_set)  # Output: True
print('grape' in fruits_set)   # Output: False

# Iterating through a set
print("Iterating through the set:")
for fruit in fruits_set:
    print(fruit)

# Creating another set for set operations
more_fruits_set = {'grape', 'kiwi', 'watermelon'}

# Union of two sets
union_set = fruits_set.union(more_fruits_set)
print("Union of sets:", union_set)  # Output: {'banana', 'apple', 'kiwi', 'grape', 'watermelon'}

# Intersection of two sets
intersection_set = fruits_set.intersection(more_fruits_set)
print("Intersection of sets:", intersection_set)  # Output: {'kiwi'}

# Difference between two sets
difference_set = fruits_set.difference(more_fruits_set)
print("Difference of sets:", difference_set)  # Output: {'banana', 'apple'}

# Checking if one set is a subset of another
is_subset = fruits_set.issubset(union_set)
print("Is fruits_set a subset of union_set?", is_subset)  # Output: True

# Checking if two sets have no elements in common
no_common_elements = fruits_set.isdisjoint(more_fruits_set)
print("Do fruits_set and more_fruits_set have no common elements?", no_common_elements)  # Output: False
