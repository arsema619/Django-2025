prices = [120, 45, 300, 85, 150]

def get_expensive_products(prices):
    expensive = []
    for price in prices:
        if price > 100:
            expensive.append(price)
    return expensive

print(get_expensive_products(prices))
