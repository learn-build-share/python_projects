# Copyright (c) LearnBuildShare
# 100+ beginner-friendly Tuple examples

# 1. Empty tuple
empty_tuple = ()
print(empty_tuple)

# 2. Single item tuple
single_item = (10,)
print(single_item)

# 3. Multiple items tuple
numbers = (1, 2, 3, 4)
print(numbers)

# 4. Tuple with strings
names = ("A", "B", "C")
print(names)

# 5. Access first element
print(numbers[0])

# 6. Access last element
print(numbers[-1])

# 7. Slicing
print(numbers[1:3])

# 8. Length
print(len(numbers))

# 9. Count an item
print(numbers.count(2))

# 10. Index of item
print(numbers.index(3))

# 11-100: more examples
examples = [
    ("apple",),
    ("banana", "mango"),
    (1, 2, 3),
    (True, False),
    (10, 20, 30, 40),
    ("x", "y"),
    ("red", "green", "blue"),
    ("one", "two", "three"),
    (1,),
    (2,),
    (3,),
    (4,),
    (5,),
    (6,),
    (7,),
    (8,),
    (9,),
    (10,),
    (11,),
    (12,),
    (13,),
    (14,),
    (15,),
    (16,),
    (17,),
    (18,),
    (19,),
    (20,),
    (21,),
    (22,),
    (23,),
    (24,),
    (25,),
    (26,),
    (27,),
    (28,),
    (29,),
    (30,),
    (31,),
    (32,),
    (33,),
    (34,),
    (35,),
    (36,),
    (37,),
    (38,),
    (39,),
    (40,),
    (41,),
    (42,),
    (43,),
    (44,),
    (45,),
    (46,),
    (47,),
    (48,),
    (49,),
    (50,),
    (51,),
    (52,),
    (53,),
    (54,),
    (55,),
    (56,),
    (57,),
    (58,),
    (59,),
    (60,),
    (61,),
    (62,),
    (63,),
    (64,),
    (65,),
    (66,),
    (67,),
    (68,),
    (69,),
    (70,),
    (71,),
    (72,),
    (73,),
    (74,),
    (75,),
    (76,),
    (77,),
    (78,),
    (79,),
    (80,),
    (81,),
    (82,),
    (83,),
    (84,),
    (85,),
    (86,),
    (87,),
    (88,),
    (89,),
    (90,),
    (91,),
    (92,),
    (93,),
    (94,),
    (95,),
    (96,),
    (97,),
    (98,),
    (99,),
    (100,),
]

for index, value in enumerate(examples, start=1):
    print(index, value)
