"""Stack implementation using a Python list."""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    stack = Stack()
    for value in [1, 2, 3, 4]:
        stack.push(value)
    print(stack.peek())
    print(stack.pop())
    print(stack.size())
