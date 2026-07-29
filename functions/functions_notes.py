# ============================================================
# Made By Learn Build Share
# 🧠 PYTHON FUNCTIONS
# "Write Once. Use Forever."
# ============================================================

"""
Imagine ordering coffee.

You don't explain the recipe every time.
You simply say:

    "One Cappuccino."

The coffee machine already knows what to do.

Functions work exactly the same way.

Instead of rewriting code,
you give it a name and call it whenever needed.
"""

# Example
def coffee():
    print("☕ Coffee Ready!")

coffee()
coffee()
coffee()

# Output
# ☕ Coffee Ready!
# ☕ Coffee Ready!
# ☕ Coffee Ready!

# ------------------------------------------------------------
# PARAMETERS vs ARGUMENTS
# ------------------------------------------------------------

"""
Think...

You book an Uber.

Driver says:
"I need Pickup Location."

Pickup Location = Parameter

You say:
"Madhapur"

Madhapur = Argument

Parameter → Placeholder
Argument  → Actual Value
"""

def book_ride(location):
    print("Driver coming to", location)

book_ride("Madhapur")

# 🎯 Interview Trap

# Q:
# Is parameter and argument same?

# ❌ No

# Parameter
# ----------
# Exists while defining function

# Argument
# ----------
# Exists while calling function

# Easy Memory:
# Parameter = Placeholder
# Argument = Actual Value

# Python already owns these
print()
len()
max()
sum()

# You own these

def salary():
    pass

def bonus():
    pass

# ⚡ Predict Output

def hello():
    print("Hello")

hello()
hello()

# Answer:
# Hello
# Hello

# 💡 Do You Know?

# Every Python program already uses functions.

print()
input()
len()
range()

# These are built-in functions.

# You were using functions before learning functions.

