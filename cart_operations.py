def add_to_cart(data, cart, item_id):
    item = next((row for row in data if row[0] == item_id), None)
    if item:
        cart.append(item)
        print("Item added to cart.")
    else:
        print("Item not found.")

def delete_from_cart(cart, item_id):
    item = next((item for item in cart if item[0] == item_id), None)
    if item:
        cart.remove(item)
        print("Item removed from cart.")
    else:
        print("Item not found in cart.")
