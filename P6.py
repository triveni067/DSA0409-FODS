prices = [50, 30, 20]
quantities = [2, 1, 3]

discount_rate = 10  # %
tax_rate = 5        # %

subtotal = sum([p*q for p, q in zip(prices, quantities)])
discount_amount = subtotal * (discount_rate / 100)
after_discount = subtotal - discount_amount
tax_amount = after_discount * (tax_rate / 100)
total_cost = after_discount + tax_amount

print("Total cost:", total_cost)
