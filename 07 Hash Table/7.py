# stock_prices = []
# with open("stock_prices.csv","r") as f:
#     for line in f:
#         day,price = line.split(",")
#         price = float(price)
#         stock_prices.append([day,price])

# print(stock_prices)

stock_prices = {}
with open("stock_prices.csv","r") as f:
    for line in f:
        day,price = line.split(",")
        price = float(price)
        stock_prices[day] = price

print(stock_prices)
print(stock_prices["march 11"])
