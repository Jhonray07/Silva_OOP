"""Order class: stores ordered items and computes the totals."""


class Order:
    DISCOUNT_THRESHOLD = 500.00
    DISCOUNT_RATE = 0.10

    def __init__(self):
        self.items = []             # attribute: list of order records

    def add_item(self, item, quantity, price):
        self.items.append({"item": item, "quantity": quantity, "price": price})

    def calculate_subtotal(self):
        return sum(i["price"] * i["quantity"] for i in self.items)

    def calculate_discount(self):
        subtotal = self.calculate_subtotal()
        if subtotal >= self.DISCOUNT_THRESHOLD:
            return subtotal * self.DISCOUNT_RATE
        return 0.0

    def calculate_total(self):
        return self.calculate_subtotal() - self.calculate_discount()