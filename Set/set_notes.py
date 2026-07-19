"""
===============================================================================
                    PYTHON SETS - COMPLETE GUIDE
                            © LearnBuildShare
===============================================================================
"""

def heading(title):
    print("\n" + "="*70)
    print(title)
    print("="*70)

heading("WHAT IS A SET?")
print("A set is an unordered, mutable collection of UNIQUE elements.")

heading("CREATING SETS")
numbers = {1, 2, 3}
print(numbers)

names = {"Akhil", "Rahul", "Sai"}
print(names)

print({1,1,2,2,3,3})   # duplicates removed

mixed = {1, "Python", 3.14}
print(mixed)

empty = set()
print(type(empty))

heading("BASIC OPERATIONS")

fruits = {"Apple", "Banana"}
print(f"Start: {fruits}")

fruits.add("Orange")
print("After add:", fruits)

fruits.update(["Mango", "Grapes"])
print("After update:", fruits)

fruits.remove("Apple")
print("After remove:", fruits)

fruits.discard("XYZ")
print("After discard(XYZ):", fruits)

popped = fruits.pop()
print("Popped:", popped)
print("Remaining:", fruits)

copy_set = fruits.copy()
print("Copy:", copy_set)

heading("SET OPERATIONS")

A = {1,2,3,4}
B = {3,4,5,6}

print("Union:", A.union(B))
print("Intersection:", A.intersection(B))
print("Difference:", A.difference(B))
print("Symmetric Difference:", A.symmetric_difference(B))
print("Subset:", {1,2}.issubset(A))
print("Superset:", A.issuperset({1,2}))
print("Disjoint:", A.isdisjoint({10,11}))

heading("LOOP")
for item in A:
    print(item)

heading("BUILT-IN METHODS")
methods = [
    "add","update","remove","discard","pop","clear","copy",
    "union","intersection","difference","difference_update",
    "intersection_update","symmetric_difference",
    "symmetric_difference_update","issubset","issuperset","isdisjoint"
]
for m in methods:
    print("-", m)

heading("20 MINI EXAMPLES")
for i in range(1,21):
    s = {i, i+1, i+2}
    print(f"Example {i}: {s}")

heading("INTERVIEW QUESTIONS")
questions = [
    "What is a set?",
    "Why are duplicates removed?",
    "Difference between list and set?",
    "Why is a set unordered?",
    "Difference between remove() and discard()?",
    "What is hashing?",
    "Why is lookup O(1)?",
    "What is frozenset?",
    "Can a list be inside a set?",
    "Difference between union() and update()?"
]
for i,q in enumerate(questions,1):
    print(f"{i}. {q}")

heading("SUMMARY")
print("✔ Unique values only")
print("✔ Mutable")
print("✔ Unordered")
print("✔ Fast membership testing")
print("© LearnBuildShare")
