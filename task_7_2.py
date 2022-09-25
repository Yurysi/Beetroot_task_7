"""
    Compute the total price of the stock where the total price is the sum
    of the price of an item multiplied by the quantity of this exact item.
    """
# Input data:

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
prices_stock = stock.copy()
for price in prices_stock:
    for r_prices in prices:
        if price == r_prices:
            prices_stock[price] = prices_stock[price] * prices[r_prices]

print(prices_stock)
