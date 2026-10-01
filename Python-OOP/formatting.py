"""Shared printing helper and width setting."""
RECEIPT_WIDTH = 42


def print_header(title):
    print("=" * RECEIPT_WIDTH)
    print(title.center(RECEIPT_WIDTH))
    print("=" * RECEIPT_WIDTH)