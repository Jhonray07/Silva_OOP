"""Fast Food Ordering System - MODULAR version (entry point)."""
from display import display_menu, print_receipt
from user_input import ask_yes_no
from orders import take_orders
from calculations import calculate_subtotal, calculate_discount


def main():
    display_menu()

    if not ask_yes_no("Would you like to place an order?"):
        print("\nThank you for visiting. Goodbye!")
        return

    orders = take_orders()
    subtotal = calculate_subtotal(orders)
    discount = calculate_discount(subtotal)

    print()
    print_receipt(orders, subtotal, discount)


if __name__ == "__main__":
    main()