"""Everything that prints to the screen."""
from config import menu, RECEIPT_WIDTH


def print_header(title):
    print("=" * RECEIPT_WIDTH)
    print(title.center(RECEIPT_WIDTH))
    print("=" * RECEIPT_WIDTH)


def display_menu():
    print_header("CLAUDE'S FAST FOOD MENU")
    print(f"{'ITEM':<28}{'PRICE':>14}")
    print("-" * RECEIPT_WIDTH)
    for item, price in menu.items():
        print(f"{item:<28}{'P' + format(price, '.2f'):>14}")
    print("=" * RECEIPT_WIDTH)
    print()


def print_receipt(orders, subtotal, discount):
    total = subtotal - discount

    print_header("CLAUDE'S FAST FOOD")
    print("      Order Receipt".center(RECEIPT_WIDTH))
    print("-" * RECEIPT_WIDTH)
    print(f"{'ITEM':<16}{'QTY':>4}{'PRICE':>10}{'TOTAL':>12}")
    print("-" * RECEIPT_WIDTH)

    for order in orders:
        item, qty, price = order["item"], order["quantity"], order["price"]
        display_name = item if len(item) <= 16 else item[:13] + "..."
        print(f"{display_name:<16}{qty:>4}{price:>10.2f}{price * qty:>12.2f}")

    print("-" * RECEIPT_WIDTH)
    print(f"{'Subtotal:':<30}{subtotal:>12.2f}")
    if discount > 0:
        print(f"{'Discount (10%):':<30}{'-' + format(discount, '.2f'):>12}")
    print("-" * RECEIPT_WIDTH)
    print(f"{'TOTAL:':<30}{total:>12.2f}")
    print("=" * RECEIPT_WIDTH)
    print("        Thank you for ordering!".center(RECEIPT_WIDTH))
    print("=" * RECEIPT_WIDTH)