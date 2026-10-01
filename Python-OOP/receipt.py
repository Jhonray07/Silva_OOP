"""Receipt class: prints an Order."""
from formatting import RECEIPT_WIDTH, print_header


class Receipt:
    def __init__(self, order):
        self.order = order

    def display(self):
        subtotal = self.order.calculate_subtotal()
        discount = self.order.calculate_discount()
        total = self.order.calculate_total()

        print_header("CLAUDE'S FAST FOOD")
        print("      Order Receipt".center(RECEIPT_WIDTH))
        print("-" * RECEIPT_WIDTH)
        print(f"{'ITEM':<16}{'QTY':>4}{'PRICE':>10}{'TOTAL':>12}")
        print("-" * RECEIPT_WIDTH)

        for o in self.order.items:
            name = o["item"] if len(o["item"]) <= 16 else o["item"][:13] + "..."
            print(f"{name:<16}{o['quantity']:>4}{o['price']:>10.2f}"
                  f"{o['price'] * o['quantity']:>12.2f}")

        print("-" * RECEIPT_WIDTH)
        print(f"{'Subtotal:':<30}{subtotal:>12.2f}")
        if discount > 0:
            print(f"{'Discount (10%):':<30}{'-' + format(discount, '.2f'):>12}")
        print("-" * RECEIPT_WIDTH)
        print(f"{'TOTAL:':<30}{total:>12.2f}")
        print("=" * RECEIPT_WIDTH)
        print("        Thank you for ordering!".center(RECEIPT_WIDTH))
        print("=" * RECEIPT_WIDTH)