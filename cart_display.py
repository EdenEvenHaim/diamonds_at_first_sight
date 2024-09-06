def show_cart_items(header, cart):
    if not cart:
        print("The cart is empty.")
    else:
        print("\nItems in Cart:")
        print("\t".join(header))
        print("-" * 70)
        for item in cart:
            print("\t".join(item))
