# Define hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2800,
    "AMZN": 130,
    "MSFT": 330
}

# Ask user for number of different stocks
num_stocks = int(input("How many different stocks do you want to enter? "))

# Track total investment and individual entries
total_investment = 0
investment_details = []

for _ in range(num_stocks):
    stock = input("Enter stock symbol (e.g., AAPL): ").upper()
    if stock not in stock_prices:
        print(f"❌ {stock} not found in price list.")
        continue
    quantity = int(input(f"Enter quantity of {stock}: "))
    price = stock_prices[stock]
    value = quantity * price
    total_investment += value
    investment_details.append(f"{stock}: {quantity} shares x ${price} = ${value}")

# Show summary
print("\n📊 Investment Summary:")
for detail in investment_details:
    print(detail)
print(f"\n💰 Total Investment: ${total_investment}")

# Optional — Save to a .txt file
save_option = input("Do you want to save the result to a file? (yes/no): ").lower()
if save_option == "yes":
    with open("investment_summary.txt", "w") as file:
        file.write("Investment Summary:\n")
        for detail in investment_details:
            file.write(detail + "\n")
        file.write(f"\nTotal Investment: ${total_investment}")
    print("✅ Summary saved to investment_summary.txt")
