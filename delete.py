# Delete From Cart:
def delete(userCart):
    item_id = input("Enter the ID of the item to delete from the cart: ")
    item = next((item for item in userCart if item[0] == item_id), None)
    if item:
        userCart.remove(item)
        print("Item removed from cart.")
    else:
        print("Item not found in cart.")