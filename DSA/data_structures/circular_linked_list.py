"""Circular linked list implementation."""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        current = self.head
        while current.next != self.head:
            current = current.next

        current.next = new_node
        new_node.next = self.head

    def traverse(self):
        if self.head is None:
            return []

        values = []
        current = self.head
        while True:
            values.append(current.data)
            current = current.next
            if current == self.head:
                break
        return values

    def delete(self, data):
        if self.head is None:
            return

        current = self.head
        previous = None

        while True:
            if current.data == data:
                if previous is None:
                    if current.next == self.head:
                        self.head = None
                        return
                    while current.next != self.head:
                        current = current.next
                    current.next = self.head.next
                    self.head = self.head.next
                    return

                previous.next = current.next
                return

            previous = current
            current = current.next
            if current == self.head:
                break


if __name__ == "__main__":
    circular = CircularLinkedList()
    for value in [10, 20, 30, 40]:
        circular.append(value)
    print(circular.traverse())
    circular.delete(20)
    print(circular.traverse())
