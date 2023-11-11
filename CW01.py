#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Get user input for the first number
num1 = float(input("Enter the first number: "))

# Get user input for the second number
num2 = float(input("Enter the second number: "))

# Calculate the sum of the two numbers
sum = num1 + num2

# Display the result
print("The sum of", num1, "and", num2, "is", sum)


# In[2]:


import math

# Get user input for the number
number = float(input("Enter a number: "))

# Calculate the square root
square_root = math.sqrt(number)

# Display the square root
print("The square root of", number, "is", square_root)



# In[4]:


# Get user input for the base and height of the triangle
base = float(input("Enter the length of the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

# Calculate the area of the triangle
area = 0.5 * base * height

# Display the area of the triangle
print("The area of the triangle is:", area)



# In[7]:


import math

# Get user input for the coefficients a, b, and c
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

# Calculate the discriminant
discriminant = b**2 - 4*a*c

# Check the discriminant to determine the number of solutions
if discriminant > 0:
    # Two real solutions
    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print("Two real solutions: x1 =", x1, "and x2 =", x2)
elif discriminant == 0:
    # One real solution
    x = -b / (2 * a)
    print("One real solution: x =", x)
else:
    # Complex solutions
    real_part = -b / (2 * a)
    imaginary_part = math.sqrt(-discriminant) / (2 * a)
    solution1 = complex(real_part, imaginary_part)
    solution2 = complex(real_part, -imaginary_part)
    print("Complex solutions: x1 =", solution1, "and x2 =", solution2)


# In[8]:


# Get user input for two variables
variable1 = input("Enter the first variable: ")
variable2 = input("Enter the second variable: ")

# Display the original values
print("Original values: variable1 =", variable1, "and variable2 =", variable2)

# Swap the values
temp = variable1
variable1 = variable2
variable2 = temp

# Display the values after swapping
print("Values after swapping: variable1 =", variable1, "and variable2 =", variable2)


# In[9]:


import random

# Generate a random integer between a specified range
random_integer = random.randint(1, 100)  # Generates a random integer between 1 and 100 (inclusive)
print("Random Integer:", random_integer)

# Generate a random floating-point number between 0 and 1
random_float = random.random()  # Generates a random floating-point number between 0 and 1
print("Random Float:", random_float)



# In[10]:


# Get user input for the distance in kilometers
kilometers = float(input("Enter the distance in kilometers: "))

# Perform the conversion to miles
miles = kilometers * 0.621371

# Display the equivalent distance in miles
print(f"{kilometers} kilometers is approximately {miles} miles")


# In[13]:


# Get user input for the temperature in Celsius
celsius = float(input("Enter the temperature in Celsius: "))

# Perform the conversion to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Display the temperature in Fahrenheit
print(f"{celsius} degrees Celsius is approximately {fahrenheit} degrees Fahrenheit")


# In[15]:


# Get user input for a number
number = float(input("Enter a number: "))

# Check if the number is positive, negative, or zero
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# In[19]:


# Get user input for a number
number = int(input("Enter a number: "))

# Check if the number is even or odd
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")


# In[18]:


# Get user input for a number
number = int(input("Enter a number: "))

# Check if the number is even or odd
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")


# In[21]:


# Get user input for a year
year = int(input("Enter a year: "))

# Check if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


# In[22]:


# Get user input for a year
year = int(input("Enter a year: "))

# Check if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


# In[23]:


# Get user input for three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Find the largest number
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

# Display the largest number
print("The largest number is:", largest)


# In[25]:


import math

def is_prime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False

    for i in range(5, int(math.sqrt(number)) + 1, 6):
        if number % i == 0 or number % (i + 2) == 0:
            return False

    return True

# Get user input for a number to check for primality
number = int(input("Enter a number: "))

if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")


# In[26]:


import math

def is_prime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False

    for i in range(5, int(math.sqrt(number)) + 1, 6):
        if number % i == 0 or number % (i + 2) == 0:
            return False

    return True

# Get user input for a number to check for primality
number = int(input("Enter a number: "))

if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")


# In[28]:


import math

def is_prime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False

    for i in range(5, int(math.sqrt(number)) + 1, 6):
        if number % i == 0 or number % (i + 2) == 0:
            return False

    return True

# Get user input for the interval
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# Ensure the interval is valid
if start < 2:
    start = 2

# Print prime numbers in the interval
print(f"Prime numbers in the interval [{start}, {end}]:")
for number in range(start, end + 1):
    if is_prime(number):
        print(number)


# In[35]:


# Get user input for a number
number = int(input("Enter a number: "))

# Initialize the factorial to 1
factorial = 1

# Calculate the factorial using a loop
if number < 0:
    print("Factorial is not defined for negative numbers.")
elif number == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, number + 1):
        factorial *= i
    print(f"The factorial of {number} is {factorial}")


# In[33]:


def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Get user input for a number
number = int(input("Enter a number: "))

result = factorial(number)
print(f"The factorial of {number} is {result}")


# In[ ]:




