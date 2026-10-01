"""Everything that asks the customer for input (with validation)."""
from config import menu


def ask_yes_no(question):
    while True:
        answer = input(question + " (yes/no): ").strip().lower()
        if answer in ("yes", "y"):
            return True
        elif answer in ("no", "n"):
            return False
        print(">> Invalid input. Please type 'yes' or 'no'.\n")


def get_menu_item():
    while True:
        item_input = input("Enter the menu item name: ").strip()
        for menu_item in menu:
            if menu_item.lower() == item_input.lower():
                return menu_item
        print(">> Item not found on the menu. Please check spelling.\n")


def get_quantity():
    while True:
        qty_input = input("Enter the quantity: ").strip()
        if qty_input.isdigit() and int(qty_input) > 0:
            return int(qty_input)
        print(">> Invalid quantity. Please enter a whole number greater than 0.\n")