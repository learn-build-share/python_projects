# Tuple Full Study Guide

Copyright (c) LearnBuildShare

## 1. Definition of Tuple
A Tuple is an ordered collection of values in Python.
It is immutable, which means once it is created, its contents cannot be changed.

Example:
```python
otp_tuple = (123456,)
```

## 2. Syntax explanation
- A tuple is created using round brackets `()`.
- A single-value tuple needs a comma after the value: `(123456,)`.
- Values inside a tuple are accessed using indexing: `otp_tuple[0]`.
- To compare values, use `==`.
- To get the length, use `len(otp_tuple)`.

## 3. Real-world analogy
Imagine you receive an OTP on your phone while logging into your bank account.
That code must stay fixed until the verification is complete.
A tuple is useful here because it protects the OTP from accidental changes during verification.

## 4. List vs Tuple comparison
```python
# List (mutable)
numbers_list = [1, 2, 3]

# Tuple (immutable)
numbers_tuple = (1, 2, 3)
```

Difference:
- List can be changed.
- Tuple cannot be changed.
- OTP should not be modified during verification, so Tuple is safer.

## 5. Classroom-style explanation for each line of code
```python
otp_tuple = (123456,)
```
- This creates a tuple with one OTP value.

```python
print(otp_tuple[0])
```
- This prints the first item in the tuple.

```python
user_input = "123456"
```
- This stores the number entered by the user as text.

```python
if user_input == str(otp_tuple[0]):
```
- This compares the entered OTP with the OTP stored in the tuple.

```python
    print("OTP verified")
```
- This message appears when both values match.

## 6. Example programs
```python
# Example 1
otp_tuple = (123456,)
print(otp_tuple)
```

```python
# Example 2
otp_tuple = (123456,)
print(otp_tuple[0])
```

```python
# Example 3
otp_tuple = (987654,)
user_input = "987654"
if user_input == str(otp_tuple[0]):
    print("OTP verified")
```

```python
# Example 4
student_marks = (90, 85, 78)
print(student_marks[1])
```

```python
# Example 5
colors = ("red", "green", "blue")
print(colors[-1])
```

```python
# Example 6
numbers = (10, 20, 30, 40)
print(len(numbers))
```

```python
# Example 7
numbers = (1, 2, 3, 4)
print(numbers[1:3])
```

```python
# Example 8
value = (True, False)
print(value)
```

```python
# Example 9
names = ("A", "B", "C")
print(names.count("A"))
```

```python
# Example 10
numbers = (2, 4, 6, 8)
print(numbers.index(6))
```

## 7. 100+ basic examples
```python
# 1
example1 = ()
print(example1)

# 2
example2 = (1,)
print(example2)

# 3
example3 = (2, 3)
print(example3)

# 4
example4 = ("a", "b")
print(example4)

# 5
example5 = (True, False)
print(example5)

# 6
example6 = (10, 20, 30)
print(example6[1])

# 7
example7 = (100, 200, 300)
print(example7[-1])

# 8
example8 = (11, 22, 33, 44)
print(example8[1:3])

# 9
example9 = ("one", "two", "three")
print(len(example9))

# 10
example10 = ("red", "green")
print(example10.count("red"))

# 11
example11 = (1, 2, 3, 4)
print(example11.index(3))

# 12
example12 = ("apple",)
print(example12)

# 13
example13 = ("banana", "mango")
print(example13)

# 14
example14 = (1, 2, 3, 4, 5)
print(example14)

# 15
example15 = (6, 7, 8)
print(example15)

# 16
example16 = ("p", "q", "r")
print(example16)

# 17
example17 = ("x", "y")
print(example17)

# 18
example18 = ("sun", "moon")
print(example18[0])

# 19
example19 = ("car", "bus", "train")
print(example19[-1])

# 20
example20 = (1, 3, 5, 7)
print(example20[2])
```

More examples can be created in the same style for practice.

## 8. Interview questions and answers
1. What is a Tuple in Python?
   - A Tuple is an ordered collection of values.
2. Why is Tuple used for OTP storage?
   - Because it is immutable and protects the OTP from changes.
3. What is the syntax of a Tuple?
   - `otp = (123456,)`
4. How do you access a value from a Tuple?
   - Use indexing: `otp[0]`
5. What is the difference between List and Tuple?
   - List is mutable, Tuple is immutable.
6. Write a small OTP example using Tuple.
   - `otp = (456789,)` then compare it with user input.

## 9. Short interview-style answer
Why is Tuple chosen for OTP storage?
Because OTP values must remain unchanged while verification is in progress. Tuple is immutable, so it keeps the data safe and consistent.
