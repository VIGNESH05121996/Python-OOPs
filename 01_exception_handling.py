"""
Here are some frequently encountered exceptions:
    ZeroDivisionError: Raised when dividing by zero.
    TypeError: Occurs when an operation is applied to an object of inappropriate type.
    ValueError: Raised when an operation receives an argument of the correct type but invalid value.
    IndexError: Occurs when accessing an invalid index in a list.
    KeyError: Raised when trying to access a dictionary key that doesn’t exist.
    FileNotFoundError: Occurs when attempting to open a non-existent file.
    ImportError: Raised when an import statement fails.
    AttributeError: Happens when an invalid attribute is accessed on an object.
    NameError: Raised when a variable or function name is not defined.
    TimeoutError: Raised when an operation times out.
"""

# Basic Exception 
try:
    x = 10 / 0  # This will cause ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero.")


# Multiple exception
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except (ZeroDivisionError, ValueError) as e:
    print(f"An error occurred: {e}")

# Catch all exception
try:
    x = 10 / 0
except Exception as e:
    print(f"An error occurred: {e}")


# use of else if no exception
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print(f"Result: {result}")

# use of finally to execute if error occurs or not
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    pass
    #file.close()  # Ensures the file is closed properly if file exists

# using raise to throw exception
def check_age(age):
    if age < 18:
        raise ValueError("Age must be at least 18.")
    return "You are allowed."

try:
    print(check_age(16))
except ValueError as e:
    print(f"Error: {e}")

#custom exception
class CustomError(Exception): # CustomError is built in exception type
    pass # here pass means custom error doesn't explicitly does any operation but still its a exception

try:
    raise CustomError("This is a custom error message.") # explicitly triggers exception
except CustomError as e:
    print(f"Caught custom exception: {e}")

