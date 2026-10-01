"""Fast Food Ordering System - OOP version (entry point).

Input prompts live here (like "Enter Name" in the lesson's main.py)
because they don't need a separate module/class.
"""
from menu import Menu
from order import Order
from receipt import Receipt

MENU_ITEMS = {
    "Cheeseburger":     89.00,
    "Chicken Sandwich": 99.00,
    "Fries (Large)":    55.00,
    "Nuggets (6pcs)":   79.00,
    "Soft Drink":       45.00,
    "Iced Tea":         40.00,
    "Sundae":           35.00,
    "Apple Pie":        39.00,
}


def ask_yes_no(question):
    while True:
        answer = input(question + " (yes/no): ").strip().lower()
        if answer in ("yes", "y"):
            return True
        elif answer in ("no", "n"):
            return False
        print(">> Invalid input. Please type 'yes' or 'no'.\n")


def get_menu_item(menu):
    while True:
        item = menu.find_item(input("Enter the menu item name: ").strip())
        if item:
            return item
        print(">> Item not found on the menu. Please check spelling.\n")


def get_quantity():
    while True:
        qty = input("Enter the quantity: ").strip()
        if qty.isdigit() and int(qty) > 0:
            return int(qty)
        print(">> Invalid quantity. Please enter a whole number greater than 0.\n")


def main():
    menu = Menu(MENU_ITEMS)          # object 1
    menu.display()

    if not ask_yes_no("Would you like to place an order?"):
        print("\nThank you for visiting. Goodbye!")
        return

    order = Order()                  # object 2
    ordering = True
    while ordering:
        print()
        item = get_menu_item(menu)
        quantity = get_quantity()
        order.add_item(item, quantity, menu.get_price(item))
        print(f">> Added: {quantity} x {item}\n")
        ordering = ask_yes_no("Would you like to order another item?")

    print()
    Receipt(order).display()         # object 3


if __name__ == "__main__":
    main()