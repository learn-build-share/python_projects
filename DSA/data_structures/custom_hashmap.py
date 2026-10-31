"""Custom hashmap implementation using separate chaining."""


class CustomHashMap:
    def __init__(self, size=16):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        bucket = self.table[self._hash(key)]
        for index, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                bucket[index] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key, default=None):
        bucket = self.table[self._hash(key)]
        for existing_key, value in bucket:
            if existing_key == key:
                return value
        return default

    def remove(self, key):
        bucket = self.table[self._hash(key)]
        for index, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                del bucket[index]
                return

    def contains(self, key):
        return self.get(key, _MISSING) is not _MISSING

    def __len__(self):
        return sum(len(bucket) for bucket in self.table)

    def items(self):
        return [item for bucket in self.table for item in bucket]


_MISSING = object()


if __name__ == "__main__":
    table = CustomHashMap()
    table.put("name", "Bob")
    table.put("age", 31)
    print(table.get("name"))
    print(table.items())
