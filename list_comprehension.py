"""Made By Learn Build Share"""

# � What is List Comprehension?
# List comprehension is a concise way to create lists in Python using a single expression.
# It combines a loop, an optional condition, and an output expression into one readable line.
# Basic syntax:
# new_list = [expression for item in iterable if condition]
# Example: squares = [x * x for x in range(1, 6)]

# ✅ Advantages:
# - Shorter and more readable than manual loops
# - Often faster than appending inside a for-loop
# - Works well for simple transformations and filtering

# ❗ Use plain loops when the expression becomes too complex or nested logic hurts readability.

# Example 1: Create a list of squares
squares = [x * x for x in range(1, 6)]
print('Squares:', squares)

# Example 2: Filter even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [n for n in numbers if n % 2 == 0]
print('Even numbers:', even_numbers)

# Example 3: Transform and filter dictionary items
students = {
    'Akhil': 90,
    'Sita': 82,
    'Ajay': 68,
    'Priya': 95,
}
# Keep student names with attendance >= 75
shortlist = [name for name, attendance in students.items() if attendance >= 75]
print('Shortlisted students:', shortlist)

# Example 4: Use if-else inside list comprehension
# Convert numbers to 'even' or 'odd'
parity = ['even' if n % 2 == 0 else 'odd' for n in numbers]
print('Parity labels:', parity)

# Example 5: Flatten a nested list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [value for row in matrix for value in row]
print('Flattened matrix:', flat)

# Interview Questions Frequently Asked
# 1. What is list comprehension in Python?
#    A concise syntax to build lists from iterables with optional filtering.
# 2. What are the parts of list comprehension?
#    expression, for-loop, and optional if condition.
# 3. Can list comprehension replace map() and filter()?
#    Yes, often with better readability, e.g. [x*2 for x in data if x > 0].
# 4. Can you use if-else inside list comprehension?
#    Yes. Use the conditional expression before the loop: [x if x > 0 else -x for x in data].
# 5. How do you flatten nested lists with list comprehension?
#    Use two for clauses: [item for sublist in nested for item in sublist].
# 6. When should you avoid list comprehension?
#    When the logic becomes too complex, nested, or hard to read. Use normal loops for clarity.

# Tip: For large datasets, a generator expression may be better than a list comprehension
# because it produces values lazily and uses less memory.
