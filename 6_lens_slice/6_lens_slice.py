## 6. Len's slice project

# Pizza toppings and prices

toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

prices = [2, 6, 1, 3, 2, 7, 2]

# Research on $2 slices 

num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

num_pizzas = len(toppings)
print("We sell " + str(num_pizzas) + " different kinds of pizzas!")

# Creating 2D list

pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
print(pizza_and_prices)

# Sorting and slicing pizzas

pizza_and_prices.sort()

cheapest_pizza = pizza_and_prices[0]

priciest_pizza = pizza_and_prices[-1]

pizza_and_prices.pop() # removing anchovies slice

pizza_and_prices.insert(4, [2.5, "peppers"]) # adding peppers

three_cheapest = pizza_and_prices[0:3]
print("The three cheapest pizzas are " + str(three_cheapest))



