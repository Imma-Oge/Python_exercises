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

# employees = [
#     ["John", 50000],
#     ["Ada", 75000],
#     ["Musa", 60000]
# ]

# employees.sort()
# print(employees)
# name_sort = sorted(employees)
# print(name_sort)

# emp_sorted1 =sorted(employees,key =lambda x: x[1])
# emp_sorted =sorted(employees,key =lambda row:row[1],reverse=True)
# print(emp_sorted)
# print(emp_sorted1)
# name_sort =sorted(employees)
# print(name_sort)



fruits = ["apple", "banana", "kiwi", "mango"]
# Sort fruits by the length of each string (shortest → longest)

fruits.sort(key = lambda x: len(x))
print(fruits)

employees = [
    ["John", 50000],
    ["Ada", 75000],
    ["Musa", 60000]
]



# Sort by salary (second element) ascending.
# Sort by name (first element) descending.

desc =sorted(employees, key = lambda x: x[1], reverse=True)
asc =sorted(employees,key = lambda x: x[1])
print(asc)
print(desc)

numbers = [10450, -5, 3, -20, 8]
# Find the number with the largest absolute value using max() and a lambda function.

lambda x :max(x)
print(max(numbers))

students = [
    ["Alice", 85, 20],
    ["Bob", 90, 19],
    ["Charlie", 85, 18]
]

# Sort students first by score descending, then by age ascending (if scores are equal).
profile = sorted(students,key = lambda row:(-row[1], row[2]))

print(profile)

temperatures_c = [0, 20, 30, -5, 15]
constant1 = 1.8
constant2 = 32

print(map(list(lambda x: float(x*constant1+constant2))))


# Convert the temperatures to Fahrenheit using a lambda function and map().
# Return the result as a list.
# Explain whether the original list temperatures_c is changed.
# constant1 = 1.8
# constant2 = 32
# print(list(map(temperatures_c,lambda x:(x*constant1 for x in temperatures_c)+constant2)))

temperatures = [30,22,35,19,40]
# print those above average:

for n in temperatures:
    if n> sum(temperatures)/len(temperatures):
        print(n)

given_number = [12,7,9,20,33,14,5]
even_num = []
# print onlly even numbers and store them in a new list
for s in given_number:
    if s%2 ==0: 
        even_num.append(s)
    print(even_num)




























