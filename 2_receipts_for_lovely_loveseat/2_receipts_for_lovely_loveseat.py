## 2. Receipts for lovely loveseat

# Description for lovely loveseat

lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."

# Price for lovely loveseat

lovely_loveseat_price = 254.00

# Description for stylish settee

stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."

# Price for stylish settee

stylish_settee_price = 180.50

# Description for luxurious lamp

luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."

# Price for luxurious lamp

luxurious_lamp_price = 52.15

## Sales tax

sales_tax = .088

### Solving problems 

## First customer 

# Total:
customer_one_total = lovely_loveseat_price + luxurious_lamp_price

# List:

customer_one_itemisation = lovely_loveseat_description + luxurious_lamp_description

# Calculating tax

customer_one_tax = customer_one_total * sales_tax 

# Total cost:
total_cost = customer_one_total + customer_one_tax

# Printing receipt:

print("Receipt: " + "Customer one items: " + customer_one_itemisation + "Customer One Total: " + str(total_cost))

