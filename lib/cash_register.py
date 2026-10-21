class CashRegister:
    def __init__(self, discount=0):
        self._items = []
        self._item_prices = []
        self._discount = 0
        self.discount = discount
        self._discount_applied = False
        self._addition_counts = []  # Tracks the quantity count per add_item action

    @property
    def items(self):
        return self._items

    @property
    def total(self):
        if not self._items:
            return 0.0

        subtotal = sum(self._item_prices)
        if self._discount > 0 and self._discount_applied:
            discount_fraction = self._discount / 100.0
            return subtotal * (1.0 - discount_fraction)
        return subtotal

    @total.setter
    def total(self, val):
        self._item_prices = [float(val)]
        self._items = ["Manual Entry"]
        self._addition_counts = [1]

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, val):
        if isinstance(val, int) and 0 <= val <= 100:
            self._discount = val
        else:
            print("Not valid discount")

    def add_item(self, item, price, quantity=1):
        qty = int(quantity)
        self._addition_counts.append(qty)  # Record how many items were added in this block
        for _ in range(qty):
            self._items.append(item)
            self._item_prices.append(float(price))

    def apply_discount(self):
        if self._discount > 0:
            self._discount_applied = True
            current_total = self.total
            
            if current_total.is_integer():
                print(f"After the discount, the total comes to ${int(current_total)}.")
            else:
                print(f"After the discount, the total comes to ${current_total:.2f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self._addition_counts:
            # Retrieve the exact quantity count added during the last action
            count_to_remove = self._addition_counts.pop()
            # Remove that exact number of entries from our active tracking lists
            for _ in range(count_to_remove):
                if self._items:
                    self._items.pop()
                    self._item_prices.pop()
