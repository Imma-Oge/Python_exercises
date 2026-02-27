"""You are going to get input from a student. And then tell them their class of grade. Ensure that you are able to filter out wrong input

3.5- 4.00 – First Class Honours
3.0-3.49 – Second Class Honours (Upper Division)
2.0-2.99 – Second Class Honours (Lower Division)
1.0-1.99 – Third Class Honours

"""

# solution
# # 
# grade = float(input("What is your grade score? "))

# if 3.5 <= grade <= 4.0:
#     print("First Class Honours")
# elif 3.0 <= grade < 3.49:  
#     print("Second Class Honours (Upper Division)")
# elif 2.0 <= grade < 2.99:   
#     print("Second Class Honours (Lower Division)")
# elif 1.0 <= grade < 2.0:
#     print("Third Class Honours")
# else:
#    print("Invalid Grade") 



# """
# Write a Python program that iterates through integers from 1 to 100.
# For each multiple of three, print "Fizz" instead of the number; 
# for each multiple of five, print "Buzz".
# For numbers that are multiples of both three and five, print "FizzBuzz".
#  """

# integers = range(1,101)

# for i in integers:
#     if i % 3 ==0:
#         print("Fizz")
#     if i % 5 ==0:
#         print("Buzz")
#     if i % 3 ==0 and i % 5 ==0:
#         print("FizzBuzz")
#     else: 
#         print(i)



# task 3 assignment

# write 12 x timestable using the 2 methods


# numbers = range(1,13)

# for number in numbers:
#     value = 12 * number
#     print(f"12 x {number} = {value}")

# method 2 

# numbers = range(1,101)

# for number in numbers:
#      value = int(number//12 )
#      if number % 12 ==0:
#             print(f"{number}/12 = {value}")



# Given the list below
# sales = [120,450,800,50,900,300]
# Write a Python code that classifies items in the list as Low, Medium, or High. 
# Also, do a count of items based on this classification and finally give a sum of items in each classification
# Key: less than 300 – low
#        > 300 <= 700 medium
# > 700 that's high

# task 2
# From temperatures = [30,22,35,19,40], print those above average.

# task 3
   # Given numbers = [12, 7, 9, 20, 33, 14, 5], print only even numbers and store them in a new list.


# sol
sales = [120,450,800,50,900,300]
category = ["Low", "Medium", "High"]

for sale in sales:
    if sale < 300:
        print(f"{sale} is {category[0]}")
    elif 300 < sale <= 700:
        print(f"{sale} is {category[1]}")
    elif sale > 700:
        print(f"{sale} is {category[2]}")

# Also, do a count of items based on this classification

low_count = 0
medium_count = 0 
high_count = 0
for sale in sales:
    if sale < 300:
        low_count += 1
    elif 300 < sale <= 700:
        medium_count += 1
    elif sale > 700:
        high_count += 1

print(f"Low: {low_count}, Medium: {medium_count}, High: {high_count}")