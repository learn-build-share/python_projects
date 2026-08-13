def outer():
    def inner():
        print("Hello from inner function")

    inner()

outer()

def discount_10():
    def apply_discount(price):
        return price * 0.9  # Apply a 10% discount

    return apply_discount

def discount_20():
    def apply_discount(price):
        return price * 0.8  # Apply a 20% discount

    return apply_discount


# Outer function
def create_discount(discount):

    # Inner function
    def calculate(price):

        # 'discount' value ni inner function remember cheskundi
        return price - (price * discount / 100)

    # Inner function ni return chestunnam
    return calculate

# 10% discount function create chestunnam
discount_10 = create_discount(10)
# 20% discount function create chestunnam
discount_20 = create_discount(20)

# ₹1000 ki 10% discount
print(discount_10(1000))
# Output: 900.0

# ₹1000 ki 20% discount
print(discount_20(1000))
# Output: 800.0