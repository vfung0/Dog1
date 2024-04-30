number = float(input("Enter a number: "))  # Convert input to a numeric value

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")

#  1: Identify the Greatest
# Prompt the user to enter three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Compare the numbers to find the largest one
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

# Print the result
print(f"The largest number among {num1}, {num2}, and {num3} is {largest}.")


# 2: Identify the Smallest
# Prompt the user to enter three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Compare the numbers to find the smallest one
if num1 <= num2 and num1 <= num3:
    smallest = num1
elif num2 <= num1 and num2 <= num3:
    smallest = num2
else:
    smallest = num3

# Print the result
print(f"The smallest number among {num1}, {num2}, and {num3} is {smallest}.")


# 3: Equality Check
# Prompt the user to enter three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Compare the numbers to find the smallest and largest ones
if num1 == num2 == num3:
    print(f"All numbers are equal: {num1}.")
elif num1 == num2 or num1 == num3 or num2 == num3:
    print(f"Two numbers are equal: {num1}, {num2}, or {num3}.")
else:
    smallest = min(num1, num2, num3)
    largest = max(num1, num2, num3)
    print(f"The smallest number is {smallest}. The largest number is {largest}.")

# Additional bonus: Print which numbers are equal
if num1 == num2:
    print(f"{num1} and {num2} are equal.")
if num1 == num3:
    print(f"{num1} and {num3} are equal.")
if num2 == num3:
    print(f"{num2} and {num3} are equal.")

    
#1: Leap Year Checker 
# Get the year from the user
year = int(input("Enter a year: "))

# Check if it's a leap year
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
    

