## 4. Sal's shipping projects 

# Defining weight variable 

weight = 8.4

# Ground shipping cost

if weight <= 2:
    cost = weight * 1.50 + 20
elif weight > 2 and weight <= 6:
    cost = weight * 3 + 20
elif weight > 6 and weight <= 10:
    cost = weight * 4 + 20
else:
    cost = weight * 4.75 + 20

print(cost)