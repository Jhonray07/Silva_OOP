"""Collects the customer's orders."""
from config import menu
from user_input import ask_yes_no, get_menu_item, get_quantity


def take_orders():
    orders = []
    ordering = True
    while ordering:
        print()
        item = get_menu_item()
        quantity = get_quantity()
        orders.append({"item": item, "quantity": quantity, "price": menu[item]})
        print(f">> Added: {quantity} x {item}\n")
        ordering = ask_yes_no("Would you like to order another item?")
    return orders