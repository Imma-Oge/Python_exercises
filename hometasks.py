# prices = [1200, 4500, 3000, 1500, 800]


# # Convert all prices from Naira to Dollars (assume 1 USD = 1500 NGN).
# # Round each result to 2 decimal places.
# # Return as a new list.

dollar_prices = [round(price / 1500, 2) for price in prices]
print(list(map(lambda n:round(n / 1500, 2),dollar_prices)))

#  #using list comprehension
new_list =[
    round(price/1500,2)
 for price in prices
 ]
print(new_list)

#3.

transactions = [500, -200, 1500, -50, 3000, -1000]

# #  Filter only valid (positive) transactions.



# # Get the total of valid transactions.
#filter logic:

for p in transactions:
    if p > 0:
        print(p)

valid_transactions = list(filter(lambda p:p>0,transactions))
print(valid_transactions)

# # Filter only refunds (negative values).

refunds = list(filter(lambda p:p<0,transactions))
print(refunds)

#4. 

names = ["Aisha", "Tunde", "Mary"]
scores = [78, 85, 90]
# # Tasks:
# # Combine them into a list of tuples.
print(list(zip(names,scores)))


#5. 

employees = [
    ["John", 50000],
    ["Ada", 75000],
    ["Musa", 60000]
]



# Sort alphabetically by name.
employees.sort()
print(employees) # modifying same object

name_sort = sorted(employees) # creating a new object variable
print(name_sort)

# Sort by salary ascending. and descending
asc =sorted(employees,key =lambda x: x[1])
desc =sorted(employees,key =lambda row:row[1],reverse=True)
print(asc)
print(desc)

#6.

fruits = ["apple", "banana", "kiwi", "mango"]
# Sort fruits by the length of each string (shortest → longest)

fruits.sort(key = lambda x: len(x))
print(fruits)


numbers = [10450, -5, 3, -20, 8]
# Find the number with the largest absolute value using max() and a lambda function.

lambda x :max(x)
print(max(numbers))

#7.
students = [
    ["Alice", 85, 20],
    ["Bob", 90, 19],
    ["Charlie", 85, 18]
]

# Sort students first by score descending, then by age ascending (if scores are equal).
profile = sorted(students,key = lambda row:(-row[1], row[2]))
print(profile)

#8.
temperatures_c = [0, 20, 30, -5, 15]
constant1 = 1.8
constant2 = 32

# Convert the temperatures to Fahrenheit using a lambda function and map().
print(map(list(lambda x: float(x*constant1+constant2))))


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

#10.

given_number = [12,7,9,20,33,14,5]
even_num = []
# print onlly even numbers and store them in a new list
for s in given_number:
    if s%2 ==0: 
        even_num.append(s)
    print(even_num)




























