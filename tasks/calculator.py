# welcome
print("Welcome to the calculator program!")

# function for calculating 
def calculate(a, b, operator):

    if (operator not in ["+", "-", "*", "/"]):
        raise ValueError("Invalid operator. Please use +, -, *, or /.")
    
    if (a is None or b is None):
        raise ValueError("Both numbers must be provided.")
    
    if (a == 0 and b == 0):
        raise ValueError("Both numbers cannot be zero.")
    
    if (operator == "+"): return a + b
    if (operator == "-"): return a - b
    if (operator == "*"): return a * b
    if (operator == "/"): 
        if (b == 0):
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b
    

# get the numbers
first, second = input("Enter two numbers: ").split()

# get the operator
operator = input("Enter the operator (+, -, *, /): ")

# print the result
try:
    result = calculate(float(first), float(second), operator)
    print(f"The result of {first} {operator} {second} = {result}")
finally:
    print("Thank you for using the calculator program!")