# prices = [1200, 4500, 3000, 1500, 800]


# # Convert all prices from Naira to Dollars (assume 1 USD = 1500 NGN).
# # Round each result to 2 decimal places.
# # Return as a new list.

# dollar_prices = [round(price / 1500, 2) for price in prices]
# print(list(map(lambda n:round(n / 1500, 2),dollar_prices)))

#  #using list comprehension
# new_list =[
#     round(price/1500,2)
#  for price in prices
#  ]
# print(new_list)

# transactions = [500, -200, 1500, -50, 3000, -1000]

# #  Filter only valid (positive) transactions.

# # Filter only refunds (negative values).

# # Get the total of valid transactions.
# for p in transactions:
#     if p > 0:
#         print(p)

# valid_transactions = list(filter(lambda p:p>0,transactions))
# print(valid_transactions)

# refunds = list(filter(lambda p:p<0,transactions))
# print(refunds)

# names = ["Aisha", "Tunde", "Mary"]
# scores = [78, 85, 90]
# # Tasks:
# # Combine them into a list of tuples.
# # Convert them into a dictionary.
# # Find the student with the highest score (without using max on scores directly).

# print(list(zip(names,scores)))




# Sort by salary ascending.
# Sort by salary descending.
# Sort alphabetically by name.

employees = [
    ["John", 50000],
    ["Ada", 75000],
    ["Musa", 60000]
]

# for m,n in employees:
print(employees[1].sort())



# print(tuple(lambda row:(row(employees))))


# # print(employees[[1:]])
# print(list(lambda row :row))

# names = ["ogechi","chizaram","david"]
# print(sorted(names,key = len))




















