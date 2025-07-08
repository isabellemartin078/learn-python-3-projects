## 7. Carly's clippers project 

## Data 

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Working with prices 

total_price = 0

for price in prices:
    total_price += price

average_price = total_price / len(prices)
print("Average Haircut Price: $" + str(average_price))

new_prices = [num - 5 for num in prices]

## Revenue

total_revenue = 0

for i in range(len(hairstyles)):
    total_revenue += (prices[i] * last_week[i])
print("Total Revenue: $" + str(total_revenue))

average_daily_revenue = total_revenue / 7
print("Average daily revenues: $" + str(average_daily_revenue))

## Advertising haircuts < 30

cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print("Haircuts under $30 : " + str(cuts_under_30))