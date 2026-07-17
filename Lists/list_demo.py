# Copyright (c) LearnBuildShare
# Definition: A list is an ordered, mutable collection of items that can hold duplicates and change over time.

# 1. Create an empty list
empty_list = []
print(empty_list)

# 2. Create a list with integers
numbers = [1, 2, 3, 4]
print(numbers)

# 3. Create a list with strings
names = ["Aman", "Bharat", "Chetan"]
print(names)

# 4. Create a list with mixed values
mixed = [10, "apple", True, 3.14]
print(mixed)

# 5. Access the first item
print(numbers[0])

# 6. Access the last item
print(numbers[-1])

# 7. Access a slice
print(numbers[1:3])

# 8. Check the length of a list
print(len(numbers))

# 9. Append an item
fruits = ["apple"]
fruits.append("banana")
print(fruits)

# 10. Append another item
fruits.append("mango")
print(fruits)

# 11. Extend with multiple items
fruits.extend(["grapes", "orange"])
print(fruits)

# 12. Insert an item at a specific position
fruits.insert(1, "kiwi")
print(fruits)

# 13. Remove an item by value
fruits.remove("banana")
print(fruits)

# 14. Remove the last item using pop
last_item = fruits.pop()
print(last_item)
print(fruits)

# 15. Clear all items
fruits.clear()
print(fruits)

# 16. Copy a list
colors = ["red", "green", "blue"]
copy_colors = colors.copy()
print(copy_colors)

# 17. Count occurrences of an item
count_value = [1, 2, 2, 3, 2].count(2)
print(count_value)

# 18. Find the index of an item
index_value = [10, 20, 30, 40].index(30)
print(index_value)

# 19. Reverse a list
numbers.reverse()
print(numbers)

# 20. Sort a list in ascending order
sorted_numbers = [4, 1, 3, 2]
sorted_numbers.sort()
print(sorted_numbers)

# 21. Sort a list in descending order
sorted_numbers.sort(reverse=True)
print(sorted_numbers)

# 22. Use max on a list
print(max([5, 8, 3, 9]))

# 23. Use min on a list
print(min([5, 8, 3, 9]))

# 24. Use sum on a list
print(sum([1, 2, 3, 4]))

# 25. Use sorted on a list
print(sorted([8, 2, 5, 1]))

# 26. Create a list from a range
print(list(range(1, 6)))

# 27. Create a list from a tuple
print(list(("a", "b", "c")))

# 28. Use list comprehension
squares = [x * x for x in range(1, 6)]
print(squares)

# 29. Use list comprehension with condition
evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)

# 30. Use enumerate
for index, value in enumerate(["a", "b", "c"]):
    print(index, value)

# 31. Use zip
for left, right in zip([1, 2, 3], [4, 5, 6]):
    print(left, right)

# 32. Check if an item exists
print(2 in [1, 2, 3])

# 33. Check if an item does not exist
print(4 not in [1, 2, 3])

# 34. Join list values into a string
print("-".join(["a", "b", "c"]))

# 35. Split a string into a list
print("python,java,cpp".split(","))

# 36. Use nested lists
matrix = [[1, 2], [3, 4]]
print(matrix[1][0])

# 37. Add a list inside a list
nested = [[1, 2, 3]]
print(nested)

# 38. Concatenate two lists
print([1, 2] + [3, 4])

# 39. Repeat a list
print(["x"] * 3)

# 40. Use list unpacking
first, second, third = [10, 20, 30]
print(first, second, third)

# 41. Use append in a loop
loop_list = []
for number in range(1, 4):
    loop_list.append(number)
print(loop_list)

# 42. Use extend in a loop
loop_list = []
for number in range(1, 4):
    loop_list.extend([number, number + 1])
print(loop_list)

# 43. Use remove after checking
items = ["a", "b", "c"]
if "b" in items:
    items.remove("b")
print(items)

# 44. Use pop with index
numbers = [10, 20, 30]
print(numbers.pop(1))
print(numbers)

# 45. Use reverse after sorting
sample = [3, 1, 2]
sample.sort()
sample.reverse()
print(sample)

# 46. Use copy to avoid aliasing
original = [1, 2, 3]
copy = original.copy()
copy.append(4)
print(original)
print(copy)

# 47. Use count with duplicates
duplicates = [1, 1, 1, 2]
print(duplicates.count(1))

# 48. Use index with a start value
print([1, 2, 3, 2].index(2, 2))

# 49. Use clear on a list
sample = [1, 2, 3]
sample.clear()
print(sample)

# 50. Use list() to convert a string to a list of characters
print(list("hello"))

# 51. Use list() to convert a set to a list
print(list({1, 2, 3}))

# 52. Use any on a list
print(any([False, True, False]))

# 53. Use all on a list
print(all([True, True, True]))

# 54. Use map with a list
print(list(map(str, [1, 2, 3])))

# 55. Use filter with a list
print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4])))

# 56. Use len on a nested list
print(len([[1], [2], [3]]))

# 57. Use max on strings
print(max(["apple", "banana", "kiwi"]))

# 58. Use min on strings
print(min(["apple", "banana", "kiwi"]))

# 59. Use sum on a list of numbers
print(sum([10, 20, 30]))

# 60. Use sorted on a list of strings
print(sorted(["z", "a", "m"]))

# 61. Use reverse on a list of strings
letters = ["b", "a", "c"]
letters.reverse()
print(letters)

# 62. Sort a list of tuples
pairs = [(2, "b"), (1, "a"), (3, "c")]
pairs.sort()
print(pairs)

# 63. Use slicing to get every second value
print([1, 2, 3, 4, 5, 6][::2])

# 64. Use slicing to reverse a list
print([1, 2, 3, 4][::-1])

# 65. Use slicing with start and stop
print([10, 20, 30, 40, 50][1:4])

# 66. Use concatenation with a tuple
print([1, 2] + list((3, 4)))

# 67. Repeat a list of strings
print(["py"] * 4)

# 68. Use a list inside a for loop
for value in [1, 2, 3]:
    print(value)

# 69. Use break inside a loop over a list
for value in [1, 2, 3, 4]:
    if value == 3:
        break
    print(value)

# 70. Use continue inside a loop over a list
for value in [1, 2, 3, 4]:
    if value == 2:
        continue
    print(value)

# 71. Use list unpacking with more values
first, *rest = [10, 20, 30, 40]
print(first)
print(rest)

# 72. Use list unpacking with starred middle values
first, *middle, last = [10, 20, 30, 40]
print(first, middle, last)

# 73. Create a list using a loop
loop_values = []
for x in range(5):
    loop_values.append(x)
print(loop_values)

# 74. Create a list using a condition inside a loop
conditional_values = []
for x in range(10):
    if x % 2 == 0:
        conditional_values.append(x)
print(conditional_values)

# 75. Use list swapping
swap_list = [1, 2]
swap_list[0], swap_list[1] = swap_list[1], swap_list[0]
print(swap_list)

# 76. Replace a value at an index
replace_list = [1, 2, 3]
replace_list[1] = 99
print(replace_list)

# 77. Compare two lists for equality
print([1, 2, 3] == [1, 2, 3])

# 78. Compare two lists for inequality
print([1, 2] != [1, 3])

# 79. Use set on a list to remove duplicates
print(list(set([1, 2, 2, 3])))

# 80. Use sorted with key parameter
print(sorted(["banana", "apple", "mango"], key=len))

# 81. Use list multiplication with a list of strings
print(["hi"] * 5)

# 82. Use list multiplication with numbers
print([0] * 5)

# 83. Use del to remove an index
days = ["Mon", "Tue", "Wed"]
del days[1]
print(days)

# 84. Use del to remove a slice
numbers = [1, 2, 3, 4, 5]
del numbers[1:3]
print(numbers)

# 85. Use append with a dictionary
data = []
data.append({"name": "Asha"})
print(data)

# 86. Create a list from a string with split
print("one two three".split())

# 87. Use sum with a list of floats
print(sum([1.5, 2.5, 3.0]))

# 88. Use max with a list of strings
print(max(["python", "java", "cpp"]))

# 89. Use min with a list of strings
print(min(["python", "java", "cpp"]))

# 90. Use enumerate with a start value
for index, value in enumerate(["x", "y", "z"], start=1):
    print(index, value)

# 91. Use zip with three lists
for a, b, c in zip([1, 2], [3, 4], [5, 6]):
    print(a, b, c)

# 92. Use all on an empty list
print(all([]))

# 93. Use any on an empty list
print(any([]))

# 94. Use list(set()) to create a unique list
print(list(set([3, 3, 3, 4])))

# 95. Use sorted on a list of numbers
print(sorted([4, 2, 1, 3]))

# 96. Use reversed on a list
print(list(reversed([1, 2, 3])))

# 97. Use list with a generator expression
print(list(x for x in range(3)))

# 98. Use a nested comprehension
print([[x, x + 1] for x in range(3)])

# 99. Use a comprehension to filter names
names = ["Asha", "Bharat", "Chetan", "Dina"]
print([name for name in names if len(name) > 4])

# 100. Use a comprehension to create uppercase names
print([name.upper() for name in names])

# 101. Use append to build a list gradually
build_list = []
for x in range(1, 6):
    build_list.append(x)
print(build_list)

# 102. Use extend to add many values at once
build_list = [1, 2]
build_list.extend([3, 4, 5])
print(build_list)

# 103. Use insert to add at the front
build_list.insert(0, 0)
print(build_list)

# 104. Use remove to drop a value
build_list.remove(0)
print(build_list)

# 105. Use pop to remove the last element
build_list.pop()
print(build_list)

# 106. Use clear to empty the list
build_list.clear()
print(build_list)

# 107. Use count on a mixed list
print([1, "1", 1, 2].count(1))

# 108. Use index on a mixed list
print(["x", "y", "z"].index("y"))

# 109. Use sort on a list of numbers
number_list = [5, 1, 4, 2]
number_list.sort()
print(number_list)

# 110. Use reverse on a list of numbers
number_list.reverse()
print(number_list)

# 111. Use copy to duplicate the list
number_copy = number_list.copy()
print(number_copy)

# 112. Use slicing to copy a list
print(number_list[:])

# 113. Use slicing to skip values
print([1, 2, 3, 4, 5, 6][::2])

# 114. Use slicing to get the middle values
print([10, 20, 30, 40, 50][1:4])

# 115. Use a list of lists
grid = [[1, 2], [3, 4], [5, 6]]
print(grid[2][0])

# 116. Flatten a nested list with a loop
flattened = []
for row in grid:
    flattened.extend(row)
print(flattened)

# 117. Use zip to combine items from lists
print(list(zip([1, 2], [3, 4])))

# 118. Use map to square numbers
print(list(map(lambda x: x * x, [1, 2, 3])))

# 119. Use filter to select even values
print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4])))

# 120. Use a literal list inside another list
print([[1, 2], [3, 4]])
