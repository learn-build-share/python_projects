"""Recursive algorithms and classic problems."""


def factorial(n):
    if n < 0:
        raise ValueError("factorial is not defined for negative numbers")
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n in (0, 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def tower_of_hanoi(disks, source='A', helper='B', target='C'):
    if disks == 1:
        return [f"Move disk 1 from {source} to {target}"]

    moves = tower_of_hanoi(disks - 1, source, target, helper)
    moves.append(f"Move disk {disks} from {source} to {target}")
    moves.extend(tower_of_hanoi(disks - 1, helper, source, target))
    return moves


if __name__ == "__main__":
    print(factorial(5))
    print(fibonacci(7))
    print(tower_of_hanoi(3))
