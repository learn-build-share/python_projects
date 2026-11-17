import sys
import time
import tracemalloc

from analyst import rupees
from lazy_reader import read_orders


def eager(path):
    with open(path, encoding="utf-8") as f:
        rows = f.readlines()[1:]
    data = [r.rstrip().split(",") for r in rows]
    return sum(int(p[2]) * int(p[3]) for p in data)


def lazy(path):
    total = 0
    for order in read_orders(path):
        p = order.rstrip().split(",")
        total += int(p[2]) * int(p[3])
    return total


def measure(fn, path):
    tracemalloc.start()
    start = time.perf_counter()
    result = fn(path)
    seconds = time.perf_counter() - start
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return result, peak / 1_000_000, seconds


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "data/orders.csv"
    for name, fn in [("Eager (readlines)", eager), ("Lazy (yield)", lazy)]:
        total, mb, sec = measure(fn, path)
        print(f"{name:<18} total={rupees(total)}  peak={mb:,.2f} MB  time={sec:.2f}s")
