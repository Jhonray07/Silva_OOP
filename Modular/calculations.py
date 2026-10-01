"""Subtotal and discount computations."""
from config import DISCOUNT_THRESHOLD, DISCOUNT_RATE


def calculate_subtotal(orders):
    return sum(o["price"] * o["quantity"] for o in orders)


def calculate_discount(subtotal):
    if subtotal >= DISCOUNT_THRESHOLD:
        return subtotal * DISCOUNT_RATE
    return 0.0