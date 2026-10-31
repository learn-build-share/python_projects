"""Searching algorithms such as linear and binary search."""


def linear_search(items, target):
    for index, value in enumerate(items):
        if value == target:
            return index
    return -1


def binary_search(items, target):
    left = 0
    right = len(items) - 1
    while left <= right:
        mid = (left + right) // 2
        if items[mid] == target:
            return mid
        if items[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    numbers = [2, 4, 6, 8, 10, 12]
    print(linear_search(numbers, 8))
    print(binary_search(numbers, 10))
