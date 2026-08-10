# password_checker.py
# ------------------
# This module demonstrates a simple password validation example using nested functions.
# It is written for learning and interview preparation, showing how inner helper
# routines can stay local to the enclosing function.
#
# Notes for fresher to experienced developers:
# - Fresher: Nested functions are defined inside other functions. They keep helper
#   logic close to the code that uses it and avoid exposing helpers at the module level.
# - Intermediate: Nested functions improve encapsulation, reduce namespace clutter,
#   and can make small validation flows easier to reason about.
# - Experienced: Use them for small, focused helpers or when closures are needed.
#   Avoid them when logic grows too large or when the helper should be reused elsewhere.
#
# Interview questions on nested functions:
# 1. What is a nested function and why would you use one?
# 2. How can a nested function access variables from the enclosing scope?
# 3. What is a closure? Give an example with a nested function returning another function.
# 4. When should you use a nested function instead of a separate helper?
# 5. How do nested functions affect code readability and unit testing?
# 6. Can nested functions be used with decorators or callbacks? Explain why.
#
# Senior advice from experience:
# - I use nested helpers for short validation workflows like this because the
#   helper functions are local and do not pollute the module namespace.
# - For reusable validation logic, I move helpers to module-level functions or a
#   dedicated utility module so tests and dependency tracing stay simple.
# - In interviews, I look for candidates who can explain the tradeoff between
#   local encapsulation and long-term maintainability.
# - Nested functions are powerful, but they should remain small, obvious, and focused.

def password_check(password):          # Outer function
    """Validate password rules and return a dictionary of results."""

    def check_length():
        """Return True if the password length is at least 8 characters."""
        return len(password) >= 8

    def check_special():
        """Return True if the password contains at least one special character."""
        return any(not c.isalnum() for c in password)

    def check_number():
        """Return True if the password contains at least one digit."""
        return any(c.isdigit() for c in password)

    return {
        "length": check_length(),
        "special": check_special(),
        "number": check_number(),
    }


def print_password_results(results: dict) -> None:
    """Print the validation results in a human-readable format."""
    print("Length:", "VALID" if results["length"] else "INVALID")
    print("Special:", "FOUND" if results["special"] else "NOT FOUND")
    print("Number:", "FOUND" if results["number"] else "NOT FOUND")
    print("Result:", "VALID" if all(results.values()) else "NOT VALID")


def main() -> None:
    password = input("Enter password: ")
    results = password_check(password)
    print_password_results(results)


if __name__ == "__main__":
    main()