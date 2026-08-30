class Cart:
    def __init__(self):
        self.cart = []

    def __str__(self):
        return f"Item: {self.cart}"

    def add(self, item):
        self.cart.append(item)

    def remove(self, item):
        self.cart.remove(item)

    def update(self, index, item):
        self.cart[index] = item

cart1 = Cart()

cart1.add("milk")
print(cart1.cart)

cart1.update(0, "apple")
print(cart1.cart)

print(cart1)

cart1.remove("apple")
print(cart1.cart)
