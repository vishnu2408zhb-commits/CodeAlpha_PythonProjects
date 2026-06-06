stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 350
}

total_investment = 0

n = int(input("How many stocks do you own? "))

for i in range(n):
    stock = input("Enter stock symbol: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock in stock_prices:
        investment = stock_prices[stock] * quantity
        total_investment += investment
    else:
        print("Stock not found!")

print("\nTotal Investment Value: $", total_investment)

with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment Value: ${total_investment}")

print("Result saved in portfolio.txt")