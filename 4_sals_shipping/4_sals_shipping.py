## 4. Sal's shipping projects 

# Defining weight variable 

weight = 8.4

# Ground shipping cost

if weight <= 2:
    gs_cost = weight * 1.50 + 20
elif weight > 2 and weight <= 6:
    gs_cost = weight * 3 + 20
elif weight > 6 and weight <= 10:
    gs_cost = weight * 4 + 20
else:
    gs_cost = weight * 4.75 + 20

print(gs_cost)

# Premium shipping cost 

gsp_cost = 125

# Drone shipping cost 

if weight <= 2:
    ds_cost = weight * 4.50
elif weight > 2 and weight <= 6:
    ds_cost = weight * 9
elif weight > 6 and weight <= 10:
    ds_cost = weight * 12
else:
    ds_cost = weight * 14.25

