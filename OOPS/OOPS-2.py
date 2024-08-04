# Python program to create a class representing a
# shopping cart.
# Include methods for adding and removing items,
# and calculating the total price.

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, price, quantity):
        if item_name in self.items:
            self.items[item_name]['quantity'] += quantity
        else:
            self.items[item_name] = {'price': price, 'quantity': quantity}

    def remove_item(self, item_name, quantity):
        if item_name in self.items:
            if self.items[item_name]['quantity'] <= quantity:
                del self.items[item_name]
            else:
                self.items[item_name]['quantity'] -= quantity

    def calculate_total(self):
        total = sum(item['price'] * item['quantity'] for item in self.items.values())
        return total

    def __str__(self):
        cart_contents = "\n".join([f"{item_name}: {item_info['quantity']} @ ${item_info['price']:.2f} each"
                                   for item_name, item_info in self.items.items()])
        total_price = f"Total price: ${self.calculate_total():.2f}"
        return f"Shopping Cart:\n{cart_contents}\n{total_price}"

# Example usage:
cart = ShoppingCart()
cart.add_item("Apple", 0.99, 3)
cart.add_item("Banana", 0.59, 5)
cart.add_item("Orange", 0.79, 2)
print(cart)

cart.remove_item("Banana", 2)
print(cart)

cart.remove_item("Apple", 3)
print(cart)

