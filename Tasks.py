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


numbers = range(1,13)

for number in numbers:
    value = 12 * number
    print(f"12 x {number} = {value}")

# method 2 

numbers = range(1,101)

for number in numbers:
     value = int(number//12 )
     if number % 12 ==0:
            print(f"{number}/12 = {value}")




       
        #python list that classifies items in the list as 
        # low,medium or high.
        #COUNT OF ITEMS BASED THIS CLASSIFICATION AND
        #SUM OF ITEMS IN EACH CLASSIFICATION

   sales = [120,450,800,50,900,300]
   category =["Low","Medium","High"]

   for item in sales:
    if item <= 300:
        category = "Low"
        print(f"{item} is classified as {category}")
    elif 300 <= item <= 700:
        category = "Medium"
        print(f"{item} is classified as {category}")
    else:
        category = "High"
         print(f"{item} is classified as {category}")


   # SOLIUTION 3 
# to print even numbers only from a list of numbers
   numbers = [12, 7, 9, 20, 33, 14, 5]
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        print(num)

print(even_numbers.append(num))

#solution2 




