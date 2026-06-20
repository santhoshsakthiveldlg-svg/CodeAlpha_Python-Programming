stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 135
}

print("Available Stocks and Prices")
for stock, price in stock_prices.items():
    print(stock, ":", price)

portfolio = {}

while True:
    stock_name = input("Enter stock name (or done to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Stock not available")
        continue

    try:
        quantity = int(input("Enter quantity: "))
        if quantity <= 0:
            print("Invalid quantity")
            continue
    except:
        print("Invalid input")
        continue

    if stock_name in portfolio:
        portfolio[stock_name] += quantity
    else:
        portfolio[stock_name] = quantity

print("Portfolio Summary")

total_investment = 0

for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_investment += value
    print(stock, qty, price, value)

print("Total Investment:", total_investment)

save_choice = input("Save result yes or no: ").lower()

if save_choice == "yes":
    file_type = input("File type txt or csv: ").lower()

    if file_type == "txt":
        file = open("portfolio.txt", "w")
        file.write("Stock Portfolio\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            file.write(stock + " " + str(qty) + " " + str(price) + " " + str(value) + "\n")
        file.write("Total " + str(total_investment))
        file.close()

    elif file_type == "csv":
        file = open("portfolio.csv", "w")
        file.write("Stock,Quantity,Price,Value\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            file.write(stock + "," + str(qty) + "," + str(price) + "," + str(value) + "\n")
        file.write("Total,,," + str(total_investment))
        file.close()

print("Program End")