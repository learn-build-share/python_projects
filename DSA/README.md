# DSA Practice

This package contains reusable Python implementations for common data structures, parsing utilities, and algorithm demonstrations.

## Folder structure

- `algorithms/` — sorting, searching, and recursive algorithms
- `basics/` — Python parsing and enumeration examples
- `data_structures/` — linked lists, stack, queue, circular list, and hashmap examples

## Examples

```python
from DSA.data_structures.stack import Stack
from DSA.data_structures.queue import Queue
from DSA.algorithms.sorting import bubble_sort

stack = Stack()
stack.push(10)
stack.push(20)
print(stack.pop())

queue = Queue()
queue.enqueue("A")
queue.enqueue("B")
print(queue.dequeue())

print(bubble_sort([5, 1, 4, 2, 3]))
```
