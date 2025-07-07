## 4. Sal's shipping projects 

# Defining weight variable 

weight = 1.5

# Ground shipping cost

if weight <= 2:
    gs_cost = weight * 1.50 + 20
elif weight > 2 and weight <= 6:
    gs_cost = weight * 3 + 20
elif weight > 6 and weight <= 10:
    gs_cost = weight * 4 + 20
else:
    gs_cost = weight * 4.75 + 20


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


## Printing off costs

print("Price with ground shipping is: $" + str(gs_cost))
print("Price with premium shipping is: $" + str(gsp_cost))
print("Price with drone shipping is: $" + str(ds_cost))

if gs_cost < gsp_cost and gs_cost < ds_cost:
    print("Ground shipping is the cheapest option")
elif gsp_cost < gs_cost and gsp_cost < ds_cost: 
    print("Ground shipping premium is the cheapest option")
elif ds_cost < gs_cost and ds_cost < gsp_cost:
    print("Drone shipping is the cheapest option")
else: 
    "There are multiple cheap options!"