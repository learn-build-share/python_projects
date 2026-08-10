"""
Made by Learn Build Share
Scope of Variables in Python

This module demonstrates Python variable scope and the LEGB lookup order:
- Local: names defined inside the current function.
- Enclosing: names in the nearest outer function scope.
- Global: module-level names.
- Built-in: Python built-in names from the builtins module.

It includes examples of nested functions, name resolution, and safe usage notes.
"""

brand = "Pushpa Brand"          # Global


def outer():
    gang = "Keshava Gang"       # Enclosing

    def inner():
        secret = "Sandalwood"   # Local

        # Python resolves names using LEGB order:
        # 1. secret -> local scope of inner
        # 2. gang   -> enclosing scope of outer
        # 3. brand  -> global scope of the module
        # 4. len    -> built-in scope
        print(secret)
        print(gang)
        print(brand)
        print(len("Pushpa"))    # Built-in

    inner()


def pushpa():
    secret = "Sandalwood"       # Local
    print(secret)


# End-to-end notes on Python scope:
# - A local variable exists only inside the function where it is defined.
# - A global variable is defined at the module level and is accessible anywhere in the module.
# - An enclosing variable is defined in an outer function and is visible to nested inner functions.
# - Built-in names are loaded from Python's built-in namespace and are used when a name is not found in local, enclosing, or global scope.
# - Assignment inside a function creates or updates a local variable unless the variable is declared with global or nonlocal.
# - Use `global` to modify a module-level variable from inside a function.
# - Use `nonlocal` to modify an enclosing scope variable from within a nested function.
# - Control structures like if, for, and while do not create a new scope in Python.
# - Avoid shadowing built-ins (for example, do not name variables `len`, `list`, `str`, etc.).
#
# Interview questions on scope:
# 1. What does LEGB stand for, and how does Python use it to resolve names?
# 2. Explain the difference between local, enclosing, global, and built-in scope.
# 3. What happens when you assign a value to a variable inside a function?
# 4. How do `global` and `nonlocal` differ, and when should you use each?
# 5. Why do control blocks like `if` and `for` not create a new local scope?
# 6. How can shadowing a built-in name cause a bug?
# 7. In the `outer`/`inner` example, which scope is `gang` found in and why?
# 8. What is a good pattern for avoiding unexpected global state in a module?

