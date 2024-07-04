#calculator

print (""""
       ++++++++++++++++++++++++
          WLCOME TO CALCULATOR
       +++++++++++++++++++++++++
""")


# Declare 5 as num_one and 4 as num_two
num_one = input(int)
num_two = 4

# Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
print(total)  # Output: 9

# Simple calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"
    
    # Using the calculator functions
num1 = 10
num2 = 5

print("Addition:", add(num1, num2))          # Output: 15
print("Subtraction:", subtract(num1, num2))  # Output: 5
print("Multiplication:", multiply(num1, num2)) # Output: 50
print("Division:", divide(num1, num2))        # Output: 2.0