"""
Made By Learn Build Share
Learn Build Share Food Delivery App

This example demonstrates how functions work by separating
each task into its own reusable function.

"""
VADLID_USERNAME = "admin"
VALID_PASSWORD = "1234"

def login():
    """
    Authenticate the user.

    Returns:
        bool: True if login is successful, otherwise False.
    """
    username = input("Username : ")
    password = input("Password : ")

    if username == VADLID_USERNAME and password == VALID_PASSWORD:
        print("\n✅ Login Successful!\n")
        return True

    print("\n❌ Invalid Username or Password.")
    return False


def show_menu():
    """
    Display the available food items.

    Returns:
        dict: Dictionary containing menu items and prices.
    """

    menu = {
        1: ("Pizza", 250),
        2: ("Burger", 150),
        3: ("Pasta", 200),
        4: ("Fries", 120),
        5: ("Cold Drink", 80),
    }

    for item_id, (food_name, price) in menu.items():
        print(f"{item_id}. {food_name:<12} ₹{price}")
    print()
    return menu


def take_order(menu):
    """
    Accept the customer's order.

    Args:
        menu (dict): Food menu.

    Returns:
        tuple: Ordered food name, quantity and price.
    """

    item_number = int(input("Select Item Number : "))
    quantity = int(input("Enter Quantity      : "))

    food_name, price = menu[item_number]

    print(f"\n🛒 Added {quantity} x {food_name} to your cart.\n")

    return food_name, quantity, price


def calculate_bill(price, quantity):
    """
    Calculate the total bill.

    Args:
        price (int): Price of one item.
        quantity (int): Number of items ordered.

    Returns:
        int: Total bill amount.
    """

    return price * quantity


def print_invoice(food_name, quantity, price, total):
    """
    Display the final invoice.
    """

    print("========== INVOICE ==========")
    print(f"Food Item : {food_name}")
    print(f"Price     : ₹{price}")
    print(f"Quantity  : {quantity}")
    print("-----------------------------")
    print(f"Total Bill: ₹{total}")
    print("=============================")


def main():
    """
    Run the Food Delivery application.
    """

    # Stop the program if login fails.
    if not login():
        return

    # Display the menu after successful login.
    menu = show_menu()

    # Take the customer's order.
    food_name, quantity, price = take_order(menu)

    # Calculate the final bill.
    total_bill = calculate_bill(price, quantity)

    # Print the invoice.
    print_invoice(food_name, quantity, price, total_bill)


# Program execution starts here.
if __name__ == "__main__":
    main()