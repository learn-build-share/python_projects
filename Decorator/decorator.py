"""
Made By Learn Build Share
This module contains a collection of common interview questions and answers
Decorator interview Q&A (20 questions)

This file contains common interview questions and concise answers about
Python decorators. Run this file to print the Q&A to the console.
"""

INTERVIEW_QA = """
Question 1: What is a decorator in Python?
Answer: A decorator is a callable that takes a function or class and returns
    a modified function or class. Decorators are used to add behavior
    to functions or methods without changing their source code.

Question 2: How do you define a simple decorator?
Answer: Define a function that accepts a function argument, define an inner
    wrapper that uses *args/**kwargs, perform pre/post actions, and
    return the wrapper. Apply with @decorator above the function.

Question 3: Why use functools.wraps in a decorator?
Answer: `functools.wraps` copies metadata (like __name__, __doc__) from the
    original function to the wrapper, preserving introspection and tools
    that rely on metadata.

Question 4: How to write a decorator that accepts arguments?
Answer: Create a decorator factory: a function that accepts the decorator
    arguments and returns the real decorator which then returns the wrapper.

Question 5: Can decorators be stacked? Which order are they applied?
Answer: Yes. If you stack `@a` above `@b`, it becomes a(b(func)). The one
    closest to the function is applied first (inner-most), and evaluation
    flows outward.

Question 6: What is a class decorator?
Answer: A class decorator is a callable that takes a class and returns a
    modified class. Useful for registering classes, adding methods, or
    modifying attributes.

Question 7: How do you decorate instance methods and class methods?
Answer: Decorate normally with @decorator above the method. For class
    methods use @classmethod (or @staticmethod) along with additional
    decorators as needed; order matters.

Question 8: How to make a decorator work with both sync and async functions?
Answer: The wrapper can detect `inspect.iscoroutinefunction(func)` and use
    `async def` wrapper to await the wrapped function, otherwise use a
    normal `def` wrapper.

Question 9: What are common use-cases for decorators?
Answer: Logging, timing, access control (authentication/authorization),
    caching, retry logic, input validation, and instrumentation.

Question 10: How to write a decorator that preserves function signature?
Answer: Use `functools.wraps` to preserve metadata and consider `functools
    update_wrapper`. For perfect signature preservation, use `inspect` and
    `functools.wraps`, or `decorator` library which preserves signature.

Question 11: How to implement a memoization (cache) decorator?
Answer: Use a dictionary keyed by args/kwargs (make them hashable) to store
    results. For production use `functools.lru_cache` which is robust.

Question 12: How to debug decorated functions when stack traces are confusing?
Answer: Use `functools.wraps` to preserve function name and docstring, and
    inspect wrapper code. Logging inside the wrapper or temporarily
    removing the decorator helps isolate issues.

Question 13: How to implement a retry decorator?
Answer: The wrapper calls the function inside a loop/try-except block,
    retrying on specified exceptions with optional backoff and max retries.

Question 14: How to create a decorator that is thread-safe?
Answer: Use thread-safe data structures or locks (e.g., `threading.Lock`) for
    shared state inside the decorator (like caches or counters).

Question 15: How to apply decorators to all functions in a module/class?
Answer: Use metaprogramming: iterate over attributes, detect callables, and
    wrap them with the decorator; or use a metaclass for classes.

Question 16: Can decorators be used with parameters like rate-limit etc.?
Answer: Yes — parameterized decorators (decorator factories) let you pass
    settings such as rate limits, timeouts, or thresholds.

Question 17: What are common pitfalls with decorators?
Answer: Forgetting `functools.wraps` (losing metadata), not handling
    *args/**kwargs correctly, breaking type hints, or making decorators
    that are not transparent to tools and debuggers.

Question 18: How do decorators interact with type hints?
Answer: Decorating can obscure a function's signature; use `typing.Callable`,
    `typing.Protocol`, or helper libraries like `typing_extensions` and
    `functools.wraps` to preserve hints where possible.

Question 19: How to remove a decorator from a function at runtime?
Answer: If the decorator stores the original function (e.g., `wrapper.__wrapped__`)
    you can access and reassign the original: `f = f.__wrapped__`. Not all
    decorators provide this.

Question 20: When should you prefer composition over decorators?
Answer: If behavior is complex or requires many configuration options, prefer
    composing small functions or classes. Decorators are best for
    cross-cutting, orthogonal concerns like logging or caching.
"""


if __name__ == "__main__":
    print(INTERVIEW_QA)

def add_extra_behavior(func): #passing front_row_access function as an argument 
    def wrapper():
        # Add extra behavior before and after the original function runs
        print("🔐 Before function runs")

        func()
        # Add extra behavior after the original function runs 
        print("✅ After function runs")

    return wrapper


@add_extra_behavior ## decorator function is applied to the original function
def front_row_access():
    print("🎬 Front row seat allotted")


front_row_access()



def vip_verification(func):
    def wrapper(name, has_vip_pass):
        # VIP pass check
        if has_vip_pass:
            return func(name)
        else:
            print("❌ VIP pass not found. Entry rejected!")
    return wrapper

@vip_verification
def front_row_access(name):
    print(f"🎬 Welcome {name}!")
    print("🔥 Front row seat allotted.")

# VIP Guest
front_row_access("Ram", True)
# Normal Guest
front_row_access("Kiran", False)

