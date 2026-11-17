import csv
import random
from pathlib import Path

ITEMS = ["Biryani", "Paneer Tikka", "Masala Dosa", "Idli Vada", "Chicken 65", "Pulao", "Gulab Jamun", "Filter Coffee"]
PRICES = [80, 120, 150, 180, 220, 260, 320]
CITIES = ["Hyderabad", "Vijayawada", "Visakhapatnam", "Warangal", "Tirupati", "Guntur"]


def generate(path="data/orders.csv", rows=1_000_000, seed=7):
    rng = random.Random(seed)
    city_rng = random.Random(seed + 1)
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["order_id", "item", "qty", "price", "city"])
        for order_id in range(1, rows + 1):
            writer.writerow([order_id, rng.choice(ITEMS), rng.randint(1, 4), rng.choice(PRICES), city_rng.choice(CITIES)])
    return path


if __name__ == "__main__":
    print("Created", generate())
