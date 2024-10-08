import random

MAX_INCREASE = 0.1
MAX_DECREASE = 0.05
MIN_PRICE = 0.01
MAX_PRICE = 1000.0
INITIAL_PRICE = 10.0
FILENAME = "stock_output.py"

out_file = open(FILENAME, 'w')
price = INITIAL_PRICE
print(f"Starting price: ${price:,.2f}")
day = 0
while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        price_change = random.uniform(-MAX_DECREASE, 0)
    day += 1
    price *= (1 + price_change)
    print(f"On day {day} price is ${price:,.2f}")

out_file.close()