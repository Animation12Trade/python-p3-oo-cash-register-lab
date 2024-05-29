#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.discount = discount

    def add_item(self, title, price, quantity=1):
        for _ in range(quantity):
            self.items.append((title, price))
            self.total += price
        return f"{quantity} {title}(s) added. Total increased to ${self.total:.2f}"

    def apply_discount(self):
        if self.discount > 0:
            self.total -= (self.total * self.discount) / 100
            return f"After the discount of {self.discount}%, the total reduces to ${self.total:.2f}."
        else:
            return "There is no discount to apply."

    def remove_item(self, title):
        removed = False
        for item in self.items[:]:  
            if item[0] == title:
                self.total -= item[1]
                self.items.remove(item)
                removed = True
        if removed:
            return f"{title} removed. New total: ${self.total:.2f}"
        else:
            return f"{title} not found in items."

    def reset_total(self):
        self.total = 0
        self.items = []
        return "Total reset to zero."

    def list_items(self):
        return self.items

    def void_last_transaction(self):
        if self.items:
            last_item = self.items.pop()
            self.total -= last_item[1]
            return f"Last transaction voided. New total: ${self.total:.2f}"
        else:
            return "No transactions to void."

    def __str__(self):
        item_list = "\n".join([f"{item[0]}: ${item[1]:.2f}" for item in self.items])
        return f"Total: ${self.total:.2f}\nItems:\n{item_list}"

