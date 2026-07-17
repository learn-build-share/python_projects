# Copyright (c) LearnBuildShare
# Definition: A list is an ordered, mutable collection of items in Python.

# A list stores multiple values in a single variable.
# Lists allow duplicate values and support indexing, slicing, and modification.

# Example 1: Create a list
numbers = [10, 20, 30]
print(numbers)

# Example 2: Access a list item by index
print(numbers[0])

# Example 3: Access the last item
print(numbers[-1])

# Example 4: Slice a list
print(numbers[1:3])

# Example 5: Change an item in a list
numbers[1] = 25
print(numbers)

# Example 6: Append an item to the end
numbers.append(40)
print(numbers)

# Example 7: Insert an item at a chosen position
numbers.insert(2, 35)
print(numbers)

# Example 8: Remove an item by value
numbers.remove(25)
print(numbers)

# Example 9: Remove the last item
numbers.pop()
print(numbers)

# Example 10: Clear the entire list
numbers.clear()
print(numbers)

# Definition: A list is mutable, which means you can change it after creation.
# Example: Update an existing element
fruits = ["apple", "banana"]
fruits[1] = "mango"
print(fruits)

# Definition: A list is ordered, so items have a fixed position.
# Example: Access by index
print(fruits[0])

# Definition: A list can contain duplicate values.
# Example: Duplicate entries are allowed
items = [1, 2, 2, 3]
print(items)

# Definition: A list supports slicing to get a sub-list.
# Example: Get the middle part
print(items[1:3])

# Definition: A list can contain different data types.
# Example: Mixed items inside one list
mixed = [1, "two", True, 3.5]
print(mixed)

# Definition: A list can hold other lists as elements.
# Example: Nested list
matrix = [[1, 2], [3, 4]]
print(matrix[1][0])

# Definition: A list can be copied to make a separate copy.
# Example: Copy a list
colors = ["red", "green", "blue"]
copy_colors = colors.copy()
print(copy_colors)

# Definition: A list can be sorted.
# Example: Sort a list of numbers
numbers = [4, 1, 3, 2]
numbers.sort()
print(numbers)

# Definition: A list can be reversed.
# Example: Reverse a list
numbers.reverse()
print(numbers)

# Definition: The len() function gives the number of items in a list.
# Example: Find the length
print(len([10, 20, 30]))

# Definition: The max() function returns the largest item.
# Example: Find the maximum value
print(max([5, 8, 3, 9]))

# Definition: The min() function returns the smallest item.
# Example: Find the minimum value
print(min([5, 8, 3, 9]))

# Definition: The sum() function adds all numeric values in a list.
# Example: Add all values
print(sum([1, 2, 3, 4]))

# Definition: The sorted() function returns a new sorted list.
# Example: Create a sorted copy
print(sorted([4, 2, 1, 3]))

# Definition: The list() function converts another iterable into a list.
# Example: Convert a tuple to a list
print(list((1, 2, 3)))

# Definition: The append() method adds one item to the end.
# Example: Add one item
team = ["A", "B"]
team.append("C")
print(team)

# Definition: The extend() method adds many items at once.
# Example: Add multiple items
team.extend(["D", "E"])
print(team)

# Definition: The insert() method adds an item at a chosen index.
# Example: Insert at the front
team.insert(0, "Z")
print(team)

# Definition: The remove() method deletes the first matching item.
# Example: Remove one item
team.remove("B")
print(team)

# Definition: The pop() method removes and returns the last item by default.
# Example: Pop the last item
print(team.pop())
print(team)

# Definition: The clear() method removes all items from the list.
# Example: Empty the list
team.clear()
print(team)

# Definition: The index() method returns the position of an item.
# Example: Find the index
print([10, 20, 30].index(20))

# Definition: The count() method counts how many times an item appears.
# Example: Count an item
print([1, 2, 2, 3].count(2))

# Definition: The sort() method arranges items in ascending order.
# Example: Sort items
values = [3, 1, 2]
values.sort()
print(values)

# Definition: The reverse() method reverses the order of items.
# Example: Reverse the order
values.reverse()
print(values)

# Definition: A list can be used in loops.
# Example: Print each item
for item in ["one", "two", "three"]:
    print(item)

# Definition: A list can be used with list comprehension.
# Example: Create squares
squares = [x * x for x in range(1, 6)]
print(squares)

# Interview Question 1: What is a list in Python?
# Answer: A list is an ordered, mutable collection of items.

# Interview Question 2: How is a list different from a tuple?
# Answer: A list is mutable, while a tuple is immutable.

# Interview Question 3: What is the difference between append() and extend()?
# Answer: append() adds one item, while extend() adds multiple items.

# Interview Question 4: What does slicing do in a list?
# Answer: Slicing returns a sub-list using start, stop, and step values.

# Interview Question 5: Why is a list useful in Python?
# Answer: It stores multiple values in one variable and allows easy updates.

# Interview Question 6: What is the use of pop()?
# Answer: pop() removes and returns the last item by default.

# Interview Question 7: What is the difference between remove() and pop()?
# Answer: remove() deletes a value by matching content, while pop() removes by index or by default the last item.

# Interview Question 8: What is list comprehension?
# Answer: List comprehension is a compact way to create lists from existing iterables.
