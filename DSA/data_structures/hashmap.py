"""HashMap implementation without using Python's built-in dictionary."""


class HashMap:
    def __init__(self, size=16):
        self.size = size
        self._buckets = [[] for _ in range(size)]

    def _index(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        bucket = self._buckets[self._index(key)]
        for index, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                bucket[index] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key, default=None):
        bucket = self._buckets[self._index(key)]
        for existing_key, value in bucket:
            if existing_key == key:
                return value
        return default

    def remove(self, key):
        bucket = self._buckets[self._index(key)]
        for index, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                del bucket[index]
                return

    def contains(self, key):
        return self.get(key, _MISSING) is not _MISSING

    def keys(self):
        values = []
        for bucket in self._buckets:
            for key, _ in bucket:
                values.append(key)
        return values

    def values(self):
        values = []
        for bucket in self._buckets:
            for _, value in bucket:
                values.append(value)
        return values

    def items(self):
        items = []
        for bucket in self._buckets:
            items.extend(bucket)
        return items

    def __len__(self):
        return sum(len(bucket) for bucket in self._buckets)

    def __repr__(self):
        return repr(self.items())


_MISSING = object()


if __name__ == "__main__":
    hash_map = HashMap()
    hash_map.put("name", "Alice")
    hash_map.put("age", 25)
    print(hash_map.get("name"))
    print(hash_map.keys())
    print(hash_map.items())
