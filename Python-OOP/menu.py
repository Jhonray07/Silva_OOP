"""Menu class: holds the items and knows how to display them."""
from formatting import RECEIPT_WIDTH, print_header


class Menu:
    def __init__(self, items):
        self.items = items          # attribute: {name: price}

    def display(self):              # method
        print_header("CLAUDE'S FAST FOOD MENU")
        print(f"{'ITEM':<28}{'PRICE':>14}")
        print("-" * RECEIPT_WIDTH)
        for item, price in self.items.items():
            print(f"{item:<28}{'P' + format(price, '.2f'):>14}")
        print("=" * RECEIPT_WIDTH)
        print()

    def find_item(self, name):
        """Return the properly-cased menu item name, or None."""
        for item in self.items:
            if item.lower() == name.lower():
                return item
        return None

    def get_price(self, item):
        return self.items[item]