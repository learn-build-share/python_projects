import time
import tracemalloc

from lazy_reader import (
    average_order_value,
    count_orders,
    first_n,
    parse,
    read_orders,
    read_uploaded,
    sales_by,
    top_items,
    total_sales,
)

HELP = (
    "Try asking:\n"
    "- Total sales entha?\n"
    "- How many orders?\n"
    "- Average order value?\n"
    "- Top items?\n"
    "- Sales by city?\n"
    "- Show first 5 orders"
)


def indian(value):
    s = f"{int(round(value))}"
    if len(s) <= 3:
        return s
    head, tail = s[:-3], s[-3:]
    parts = []
    while len(head) > 2:
        parts.insert(0, head[-2:])
        head = head[:-2]
    if head:
        parts.insert(0, head)
    return ",".join(parts) + "," + tail


def rupees(value):
    return "₹" + indian(value)


def detect_intent(question):
    q = question.lower()
    if "city" in q or "cities" in q:
        return "city"
    if "item" in q or "top" in q or "best" in q:
        return "items"
    if "average" in q or "avg" in q:
        return "average"
    if "count" in q or "how many" in q or "orders entha" in q or "number of orders" in q:
        return "count"
    if "first" in q or "show" in q or "preview" in q:
        return "preview"
    if "total" in q or "sales" in q or "revenue" in q:
        return "total"
    return "help"


def answer(question, source):
    intent = detect_intent(question)
    if intent == "help":
        return {"text": HELP, "intent": intent, "peak_mb": 0.0, "seconds": 0.0}

    def orders():
        lines = read_uploaded(source) if hasattr(source, "read") else read_orders(source)
        return parse(lines)

    tracemalloc.start()
    start = time.perf_counter()

    if intent == "total":
        text = f"Total Sales: {rupees(total_sales(orders()))}"
    elif intent == "count":
        text = f"Total Orders: {indian(count_orders(orders()))}"
    elif intent == "average":
        text = f"Average Order Value: {rupees(average_order_value(orders()))}"
    elif intent == "items":
        rows = top_items(orders())
        text = "Top Items (by quantity):\n" + "\n".join(f"{i}. {name} - {indian(qty)}" for i, (name, qty) in enumerate(rows, 1))
    elif intent == "city":
        rows = sales_by(orders(), "city")
        text = "Sales by City:\n" + "\n".join(f"- {city}: {rupees(v)}" for city, v in rows.items())
    else:
        rows = list(first_n(orders(), 5))
        text = "First 5 orders:\n" + "\n".join(
            f"#{o['order_id']} {o['item']} x{o['qty']} @ {rupees(o['price'])} ({o['city']})" for o in rows
        )

    seconds = time.perf_counter() - start
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return {"text": text, "intent": intent, "peak_mb": peak / 1_000_000, "seconds": seconds}


if __name__ == "__main__":
    import sys

    path = sys.argv[1] if len(sys.argv) > 1 else "data/orders.csv"
    for q in ["Total sales entha?", "How many orders?", "Average order value?", "Top items?", "Sales by city?", "Show first 5 orders"]:
        result = answer(q, path)
        print(f"Q: {q}\n{result['text']}\n(peak memory: {result['peak_mb']:.2f} MB, time: {result['seconds']:.2f}s)\n")
