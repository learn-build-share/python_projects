import csv
import io
from collections import Counter, defaultdict


def read_orders(file):
    with open(file, encoding="utf-8") as f:
        next(f)
        for order in f:
            yield order


def read_uploaded(uploaded_file):
    uploaded_file.seek(0)
    text = io.TextIOWrapper(uploaded_file, encoding="utf-8", newline="")
    try:
        next(text)
        for order in text:
            yield order
    finally:
        text.detach()


def parse(lines):
    for row in csv.reader(lines):
        if len(row) < 4:
            continue
        yield {
            "order_id": int(row[0]),
            "item": row[1],
            "qty": int(row[2]),
            "price": int(row[3]),
            "city": row[4] if len(row) > 4 else "",
        }


def amounts(orders):
    for order in orders:
        yield order["qty"] * order["price"]


def total_sales(orders):
    return sum(amounts(orders))


def count_orders(orders):
    return sum(1 for _ in orders)


def average_order_value(orders):
    total = count = 0
    for amount in amounts(orders):
        total += amount
        count += 1
    return total / count if count else 0


def sales_by(orders, key):
    totals = defaultdict(int)
    for order in orders:
        totals[order[key]] += order["qty"] * order["price"]
    return dict(sorted(totals.items(), key=lambda kv: kv[1], reverse=True))


def top_items(orders, n=3):
    counter = Counter()
    for order in orders:
        counter[order["item"]] += order["qty"]
    return counter.most_common(n)


def first_n(orders, n=5):
    for i, order in enumerate(orders):
        if i >= n:
            return
        yield order
